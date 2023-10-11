import datetime
import os


class Logger:
    def __new__(cls, directory):
        if not hasattr(cls, 'instance'):
            logger = super(Logger, cls).__new__(cls)
            now_date = datetime.datetime.utcnow().strftime("%Y_%m_%d.%H.%M.%S")
            logger.file_name = f"{directory}/Logs/log_{now_date}.log"

            cls.instance = logger
        return cls.instance

    def write_log_to_file(self, data: str):
        with open(self.file_name, 'a', encoding='utf=8') as logger_file:
            logger_file.write(data)

    def add_request(self, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += "\n"

        self.write_log_to_file(data_to_add)

    def add_response(self, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += f"\n-----\n"

        self.write_log_to_file(data_to_add)