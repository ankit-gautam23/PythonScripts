import requests
import time
import threading

api_list = [
    'https://api.example.com/endpoint1',
    'https://api.example.com/endpoint2',
    'https://api.example.com/endpoint3',
]

num_tests = 10

def test_api(api):
    response_times = []

    for i in range(num_tests):
        start_time = time.time()
        response = requests.get(api)
        end_time = time.time()

        response_time = (end_time - start_time) * 1000
        response_times.append(response_time)

    avg_response_time = sum(response_times) / len(response_times)

    print(f'API: {api}')
    print(f'Average response time: {avg_response_time:.2f} ms\n')

# Loop through the API list and test each API using a separate thread
threads = []
for api in api_list:
    thread = threading.Thread(target=test_api, args=(api,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()
