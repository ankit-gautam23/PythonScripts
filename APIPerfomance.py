import requests
import time

api_list = [
    'https://api.example.com/endpoint1',
    'https://api.example.com/endpoint2',
    'https://api.example.com/endpoint3',
]

num_tests = 10

for api in api_list:
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
