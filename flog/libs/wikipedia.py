import requests


def random_article():
    url = f'https://en.wikipedia.org/api/rest_v1/page/random/title'
    return requests.get(url, timeout=2.0).json()
