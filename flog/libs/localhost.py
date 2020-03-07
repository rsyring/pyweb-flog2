import requests


def fetch_page():
    url = f'http://localhost:5000/'
    text = requests.get(url, timeout=2.0).text
    return(text)
