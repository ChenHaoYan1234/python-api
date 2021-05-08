import requests


def register(host: str, port: int, username: str, password: str, email: str = None):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    data = {
        'username': username,
        'password': password,
        'email': email,
    }
    url = host + ':' + str(port) + 'api//v1//register'
    response = requests.post(url=url, data=data, header=header)
    if response.status_code != 200:
        exit(0)


def login(host: str, port: int, username: str, password: str):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }
    data = {
        'username': username,
        'password': password,
    }
    url = host + ':' + str(port) + 'api//v1//login'
    response = requests.post(url=url, data=data, header=header)
