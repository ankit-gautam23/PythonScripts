import re
import requests

def extract_error(response_body):
    # Regex pattern to match error message
    pattern = r'"error":\s*"(.+?)"'

    # Find error message in response body
    match = re.search(pattern, response_body)

    if match:
        # Extract error message from match object
        error_message = match.group(1)

        # Search Stack Overflow for solution
        stack_overflow_solution = search_stack_overflow(error_message)

        # Search GitHub for solution
        github_solution = search_github(error_message)

        # Suggest solutions based on error type
        if "Unauthorized" in error_message:
            return "Make sure you are authenticated and have the necessary permissions.", stack_overflow_solution, github_solution
        elif "Not Found" in error_message:
            return "Make sure the resource you are trying to access exists and you have the correct URL.", stack_overflow_solution, github_solution
        elif "Validation Failed" in error_message:
            return "Check the parameters you are sending and make sure they are valid.", stack_overflow_solution, github_solution
        else:
            return "Sorry, I couldn't find a solution for this error. Please check the error message and try again.", stack_overflow_solution, github_solution
    else:
        return "No error message found in response.", None, None


def search_stack_overflow(query):
    # Stack Overflow API endpoint for search
    stack_overflow_url = "https://api.stackexchange.com/2.3/search"

    # Parameters for search query
    params = {
        "order": "desc",
        "sort": "votes",
        "intitle": query,
        "site": "stackoverflow"
    }

    # Send GET request to Stack Overflow API
    response = requests.get(stack_overflow_url, params=params)

    # Parse response for most relevant answer
    if response.ok and len(response.json()["items"]) > 0:
        answer = response.json()["items"][0]["link"]
        return answer
    else:
        return "Sorry, no solution found on Stack Overflow."


def search_github(query):
    # GitHub API endpoint for search
    github_url = "https://api.github.com/search/code"

    # Parameters for search query
    params = {
        "q": query,
        "sort": "score",
        "order": "desc",
    }

    # Headers for authentication
    headers = {
        "Authorization": "Bearer YOUR_GITHUB_TOKEN"
    }

    # Send GET request to GitHub API
    response = requests.get(github_url, params=params, headers=headers)

    # Parse response for most relevant answer
    if response.ok and len(response.json()["items"]) > 0:
        answer = response.json()["items"][0]["html_url"]
        return answer
    else:
        return "Sorry, no solution found on GitHub."


# Example usage
response_body = '{"error": "Unauthorized"}'
error_solution, stack_overflow_solution, github_solution = extract_error(response_body)
print(error_solution) # Output: "Make sure you are authenticated and have the necessary permissions."
print(stack_overflow_solution) # Output: Link to the most relevant Stack Overflow answer
print(github_solution) # Output: Link to the most relevant GitHub code repository
