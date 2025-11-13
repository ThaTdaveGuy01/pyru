import timeit
import subprocess
import os
from scraper import run_scrape

# --- Benchmark Configuration ---
PORT = 8000
BASE_URL = f"http://127.0.0.1:{PORT}"
TEST_URL = f"{BASE_URL}/test_page.html"
RUNS = 100
SELECTOR = "p.item"

def run_pyweb_benchmark():
    """Runs the benchmark for the pyweb scraper."""
    urls = [TEST_URL] * RUNS
    run_scrape(urls, SELECTOR)

def main():
    """Main function to run the benchmarks."""
    server_process = None
    try:
        # Start the local HTTP server
        server_path = os.path.join(os.path.dirname(__file__), 'http_server.py')
        server_process = subprocess.Popen(['python', server_path])
        
        # Give the server a moment to start
        import time
        time.sleep(1)

        # --- Run pyweb benchmark ---
        pyweb_time = timeit.timeit(run_pyweb_benchmark, number=1)
        
        print("\n--- Benchmark Results ---")
        print(f"pyweb ({RUNS} runs): {pyweb_time:.4f} seconds")

finally:
        if server_process:
            server_process.terminate()

if __name__ == "__main__":
    main()

