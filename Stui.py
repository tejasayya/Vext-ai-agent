import requests
import json
import streamlit as st

API_KEY = "T8eM1WDo.P72qJvM8OleJC6lR1K9LKVnF2iaFFUF3"

URL = "https://payload.vextapp.com/hook/0RK7MHNLE5/catch/hello"
headers = {
    "content-Type": "application/json",
    "Apikey": f"Api-Key {API_KEY}"
}

st.title("Chat with Teja 🤖")



# Add a text input for the user to type their question
user_input = st.text_input("Ask me anything about Teja:")

# If the user submits a question
if user_input:
    # Prepare the payload for the API request
    data = {"payload": user_input}

    # Make the API request
    response = requests.post(URL, headers=headers, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        response_json = response.json()

        # Extract the "text" field from the response
        if "text" in response_json:
            teja_response = response_json["text"]
            # Display the response from the API
            st.success("Response from Teja:")
            st.write(teja_response)
        else:
            st.error("Error: 'text' field not found in the response.")
    else:
        # Display an error message if the request failed
        st.error(f"Error: {response.status_code} - {response.text}")



# # data = {"payload": "What do you do Teja?"}
# if user_input:
#     # Prepare the payload for the API request
#     data = {
#         "payload": user_input,
#         "query": user_input
#         }

#     # Make the API request
#     response = requests.post(URL, headers=headers, json=data)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Display the response from the API
#         st.success("Response from Teja:")
#         st.write(response.text)
#     else:
#         # Display an error message if the request failed
#         st.error(f"Error: {response.status_code} - {response.text}")



