# Here's an example Python script that creates a new collection and runs a series of requests for a given endpoint

import postman_api

# Create a new Postman API client and authenticate using your API key
client = postman_api.PostmanClient(api_key='your-api-key')

# Define the name of the collection and create it
collection_name = 'My Flask API Collection'
collection = client.collections.create_collection(name=collection_name)

# Define the endpoint to test and create requests for it
endpoint_url = 'http://localhost:5000/api'
request_methods = ['GET', 'POST', 'PUT', 'DELETE']
for method in request_methods:
    request_name = f'{method} {endpoint_url}'
    request = collection.requests.create_request(
        name=request_name,
        method=method,
        url=endpoint_url,
        headers={
            'Content-Type': 'application/json',
            'Authorization': 'Bearer your-token'
        },
        body={
            'param1': 'value1',
            'param2': 'value2'
        }
    )

# Run the collection and display the results
environment = client.environments.get_environment_by_name('My Environment')
run = collection.run(environment=environment)
for result in run.results:
    print(result.request.name, result.response.status_code)
