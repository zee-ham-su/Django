from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.
def about(request):
    my_info = {
        'gender': 'Male',
        'github_url': 'https://github.com/zee-ham-su',
        'name': 'Sufian Hamza',
    }
    return JsonResponse(my_info)


def submit_data(request):
    # Example data to be submitted in the POST request
    data_to_submit = {'key1': 'value1', 'key2': 'value2'}

    # Make a POST request to the live submission link
    submission_url = 'https://backend-test-pfm3.onrender.com/data'
    response = requests.post(submission_url, json=data_to_submit)

    # Check if the POST request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and return it
        api_response = response.json()
        return JsonResponse(api_response)
    else:
        # If the POST request was not successful, return an error message
        error_message = {
            'error': 'Failed to submit data to the live submission link'}
        return JsonResponse(error_message, status=500)
