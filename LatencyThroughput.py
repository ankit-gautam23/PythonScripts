import requests
import time

API_ENDPOINT = "https://api.example.com"

# def measure_latency():
#     latencies = []
#     for i in range(10):
#         start_time = time.time()
#         response = requests.get(API_ENDPOINT)
#         end_time = time.time()
#         latency = end_time - start_time
#         latencies.append(latency)
#         print(f"Request {i+1}: {latency:.4f} seconds")
#     average_latency = sum(latencies) / len(latencies)
#     print(f"Average latency: {average_latency:.4f} seconds")


def measure_latency():
    latencies = []
    with requests.Session() as session:
        for i in range(10):
            start_time = time.time()
            response = session.get(API_ENDPOINT)
            end_time = time.time()
            latency = end_time - start_time
            latencies.append(latency)
            print(f"Request {i+1}: {latency:.4f} seconds")
    average_latency = sum(latencies) / len(latencies)
    print(f"Average latency: {average_latency:.4f} seconds")
    
    
def measure_throughput():
    with requests.Session() as session:
        start_time = time.time()
        for i in range(10):
            response = session.get(API_ENDPOINT)
        end_time = time.time()
        total_time = end_time - start_time
        throughput = 10 / total_time
        print(f"Throughput: {throughput:.2f} requests/second")

measure_latency()
measure_throughput()
