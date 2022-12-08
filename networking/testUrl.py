import requests

URL = input('url to consult ->')

try:
    response = requests.head(URL)
except Exception as e:
    print(f"NOT OK: {str(e)}")
else:
    if response.status_code == 200:
        print("This website is working...")
    else:
        print(f"NOT OK: HTTP response code {response.status_code}")