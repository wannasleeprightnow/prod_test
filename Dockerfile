FROM python:3.12

RUN mkdir /code

WORKDIR /code

COPY poetry.lock pyproject.toml .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install poetry

RUN poetry install

COPY . .

WORKDIR src

CMD poetry run uvicorn app:app --workers 10 --host=0.0.0.0 --port=8080