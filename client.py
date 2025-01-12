import requests

response = requests.get('https://www.jio.com/help/home#/')

if response.status_code == 200:
    print(response.json())

else:
    print(f"Error: {response.status_code}")


