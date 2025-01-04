import requests
import json

API_KEY = "T8eM1WDo.P72qJvM8OleJC6lR1K9LKVnF2iaFFUF3"

URL = "https://payload.vextapp.com/hook/0RK7MHNLE5/catch/resteja"
headers = {
    "content-Type": "application/json",
    "Apikey": f"Api-Key {API_KEY}"
}
data = {"payload": "What do you do Teja?"}

response = requests.post(URL, headers = headers, json = data)


print(response.text)