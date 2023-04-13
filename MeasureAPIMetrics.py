import requests

API_ENDPOINT = "https://api.example.com/metrics"

def check_api_metrics():
    response = requests.get(API_ENDPOINT)
    response.raise_for_status()
    data = response.json()
    metric1 = data['metric1']
    metric2 = data['metric2']
    if metric1 > 1000:
        print("Metric1 is higher than expected.")
    if metric2 < 50:
        print("Metric2 is lower than expected.")

check_api_metrics()
