import requests
import json

# Define the URL for the API endpoint
url = "http://localhost:11434/api/generate"

# Prepare the payload with the model and prompt
payload = {
    "model": "llama3.2:1b",
    "prompt": "What is Google's stock price?",
}

# Set the headers for the request
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, json=payload, headers=headers, stream=True)

# Check if the response was successful (status code 200)
if response.status_code == 200:
    combined_response = ""  # To hold the concatenated text
    
    try:
        # If the response is streamed, handle each JSON chunk
        for chunk in response.iter_lines():
            if chunk:
                # Decode and parse each chunk as JSON
                try:
                    response_data = json.loads(chunk.decode('utf-8'))
                    # Extract the 'response' text or the content you want to combine
                    if 'response' in response_data:
                        combined_response += response_data['response'] + " "
                except json.JSONDecodeError:
                    print("Error parsing chunk:", chunk.decode('utf-8'))

        # Print the combined response string
        print("Combined response text from Llama model:")
        print(combined_response.strip())
    except Exception as e:
        print(f"Error while processing the response: {e}")
else:
    # Print the error if response is not successful
    print(f"Failed to get a response. Status code: {response.status_code}")
    print("Response content:", response.text)
