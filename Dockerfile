FROM python
COPY requirements.txt .
WORKDIR /test_project/
RUN pip install -r /requirements.txt
CMD pytest -v --alluredir=allure_test_results/ /test_project/tests