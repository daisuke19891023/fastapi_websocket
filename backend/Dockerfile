FROM python:3.9.1-buster AS builder

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv \
    && pipenv install --system


FROM python:3.9.1-slim-buster

ENV PYTHONUNBUFFERED=1

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

COPY . ./
EXPOSE 8080

CMD ["python", "src/main.py"]
