FROM ghcr.io/binkhq/python:3.9

WORKDIR /app
ADD . .

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile && \
    apt-get update && apt-get -y install postgresql-client-14 && \
    rm -rf /var/lib/apt/lists/*

CMD [ "python", "main.py" ]
