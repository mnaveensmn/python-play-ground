import requests
import concurrent.futures
import time
from datetime import datetime
import threading

# Base URL for the endpoint
BASE_URL = "https://leads-shared-service-dev.css.rxweb-dev.com/ping"
#BASE_URL = "https://leads-shared-service-perf.css.rxweb-dev.com/ping"
#BASE_URL = "http://localhost:5055/v1/exhibitors/test"
#BASE_URL = 'https://qr-manager-service-perf.css.rxweb-dev.com/v1/exhibitors/test'
#QUERY_PARAM = 'includePublishedProductDocuments=true'
#BASE_URL = 'https://qr-manager-service-perf.css.rxweb-dev.com'
#BASE_URL = "http://localhost:5047/v1/exhibitors/test"

# List of exhibitor IDs
EXHIBITOR_IDS = [
    "exh-perf-test-AUTOM23-42",
    "exh-perf-test-AUTOM23-37",
    "exh-perf-test-AUTOM23-30",
    "exh-perf-test-AUTOM23-34",
    "exh-perf-test-AUTOM23-29",
    "exh-perf-test-AUTOM23-32",
    "exh-perf-test-AUTOM23-44",
    "exh-perf-test-AUTOM23-35",
    "exh-perf-test-AUTOM23-28",
    "exh-perf-test-AUTOM23-41",
    "exh-perf-test-AUTOM23-45",
    "exh-perf-test-AUTOM23-33",
    "exh-perf-test-AUTOM23-40",
    "exh-perf-test-AUTOM23-38",
    "exh-perf-test-AUTOM23-27",
    "exh-perf-test-AUTOM23-43",
    "exh-perf-test-AUTOM23-39",
    "exh-perf-test-AUTOM23-46",
    "exh-perf-test-AUTOM23-47",
    "exh-perf-test-AUTOM23-26",
    "exh-perf-test-AUTOM23-36",
    "exh-perf-test-AUTOM23-48",
    "exh-perf-test-AUTOM23-25",
    "exh-perf-test-AUTOM23-31"
]

EXHIBITOR_IDS_1 = [
    "exh-perf-test-AUTOM23-42"
]

def fetch_exhibitor_data(exhibitor_id, thread_id):
    #url = f"{BASE_URL}/{exhibitor_id}?{QUERY_PARAM}"
    #url = f"{BASE_URL}/{exhibitor_id}"
    url = f"{BASE_URL}"
    start_time = time.perf_counter()
    try:
        response = requests.get(url, timeout=30)  # Added a timeout
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f'{datetime.now()}\tThreadId:{thread_id}\t{url}\t{duration * 1000:.3f}\tms\t\t{response.status_code}')
    except requests.exceptions.RequestException as e:
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f'ThreadId:{thread_id}, {url}, {duration * 1000:.3f}ms, {str(e)}')


def run_in_thread(thread_id):
    for exhibitor_id in EXHIBITOR_IDS:
        fetch_exhibitor_data(exhibitor_id, thread_id)
    return "Completed"


def make_concurrent_request():
    MAX_WORKERS = 500

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_id = {executor.submit(run_in_thread, thread_id): thread_id for thread_id in range(1,MAX_WORKERS+1)}

        for future in concurrent.futures.as_completed(future_to_id):
            thread_id = future_to_id[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f"Exhibitor {thread_id} generated an exception: {exc}")

    end_time = time.time()
    print(f"\nAll data fetched in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    # for i in range(50):
    #     run_in_thread(i)
    print(f'Time\t\t\t\t\t\tThreadId\tURL\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tDuration\tResponseCode\tError')
    make_concurrent_request()

