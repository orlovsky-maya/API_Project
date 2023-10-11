import requests


class HttpMethods:
    def __init__(self, logger):
        self.headers = {'Content-Type': 'application/json'}
        self.cookie = ""
        self.logger = logger

    def get(self, url):
        self.logger.add_request(url, method='GET')
        result = requests.get(url, headers=self.headers, cookies=self.cookie)
        self.logger.add_response(result)
        return result

    def post(self, url, body):
        self.logger.add_request(url, method='POST')
        result = requests.post(url, json=body, headers=self.headers, cookies=self.cookie)
        self.logger.add_response(result)
        return result

    def put(self, url, body):
        self.logger.add_request(url, method='PUT')
        result = requests.put(url, json=body, headers=self.headers, cookies=self.cookie)
        self.logger.add_response(result)
        return result

    def delete(self, url, body):
        self.logger.add_request(url, method='DELETE')
        result = requests.delete(url, json=body, headers=self.headers, cookies=self.cookie)
        self.logger.add_response(result)
        return result
