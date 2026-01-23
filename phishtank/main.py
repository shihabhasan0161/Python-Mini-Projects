import requests

def main(url):
    endpoint = "https://checkurl.phishtank.com/checkurl/"
    headers = {
        "User-Agent": "phishtank/apicall"
    }

    data = {
        "url": url,
        "format": "json"
    }
    response = requests.post(endpoint, data=data, headers=headers)
    return response.json()

user_input = input("Enter the url to check: ")
print(main(user_input))