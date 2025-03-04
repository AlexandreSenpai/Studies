FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry install

EXPOSE 8080

CMD ["poetry", "run", "uvicorn", "--port", "8080", "--host", "0.0.0.0", "src:server"]