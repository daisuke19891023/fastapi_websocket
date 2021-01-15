FROM python:3.9.1-slim-buster

WORKDIR /app

COPY . .
RUN pip install pipenv 
RUN pipenv install --system


EXPOSE 8501
RUN echo "BACKEND_URL=http://backend:8080" > ./src/.env

CMD ["streamlit", "run", "src/main.py"]