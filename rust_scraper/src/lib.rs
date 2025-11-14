use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use scraper::{Html, Selector};
use reqwest;
use futures::future::join_all;

async fn fetch_and_parse(client: &reqwest::Client, url: String, selector_str: String) -> Result<Vec<String>, reqwest::Error> {
    let body = client.get(&url).send().await?.text().await?;
    
    let result = tokio::task::spawn_blocking(move || {
        let fragment = Html::parse_document(&body);
        let sel = Selector::parse(&selector_str).unwrap();
        fragment.select(&sel)
            .map(|element| element.text().collect::<String>())
            .collect()
    }).await.unwrap();

    Ok(result)
}

async fn scrape_all_urls(urls: Vec<String>, selector: String) -> PyResult<Vec<Vec<String>>> {
    let client = reqwest::Client::new();
    
    let futures = urls.into_iter().map(|url| {
        let client = client.clone();
        let selector = selector.clone();
        async move {
            fetch_and_parse(&client, url, selector).await
        }
    });

    let results = join_all(futures).await;

    let mut final_results = Vec::new();
    for result in results {
        match result {
            Ok(elements) => final_results.push(elements),
            Err(e) => return Err(pyo3::exceptions::PyConnectionError::new_err(e.to_string())),
        }
    }

    Ok(final_results)
}

#[pyfunction]
fn scrape_urls_concurrent(py: Python, urls: Vec<String>, selector: String) -> PyResult<&PyAny> {
    pyo3_asyncio::tokio::future_into_py(py, async move {
        scrape_all_urls(urls, selector).await
    })
}

#[pymodule]
fn rust_scraper(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(scrape_urls_concurrent, m)?)?;
    Ok(())
}