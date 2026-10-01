import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    joke_data = response.json()
    print(f"Joke: {joke_data['setup']} - {joke_data['punchline']}")

else:
    print("Error 404: Failed to receive joke")