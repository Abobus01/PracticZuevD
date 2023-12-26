FROM python:3.8

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY allure-results .

CMD ["python", "run_tests.py"]
