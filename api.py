import requests

DEFAULT_TOKEN =
default_headers = {"X-Risk-Token": DEFAULT_TOKEN,
                   "Content-type": "application/json"}


def get(url, headers=default_headers):

    response = requests.get(url, headers=headers)

    return response


def post(url, payload, headers=default_headers):

    response = requests.post(url, json=payload, headers=headers)

    return response


def put(url, payload, headers=default_headers):

    response = requests.put(url, json=payload, headers=headers)

    return response


def delete(url, headers=default_headers):

    response = requests.delete(url, headers=headers)

    return response



