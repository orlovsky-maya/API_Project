FROM python:3.10-alpine
COPY requirements.txt .
WORKDIR /test_project/
RUN pip install -r /requirements.txt
CMD ./run_pytest.sh