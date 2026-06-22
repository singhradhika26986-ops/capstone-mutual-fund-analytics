import requests

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

if response.status_code == 200:
    print("Live NAV fetched successfully")
    print(response.json())
else:
    print("Failed to fetch data")