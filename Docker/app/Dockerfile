FROM python:3.12

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /api/requirements.txt

COPY ./app /api/app

CMD ["fastapi", "run", "app/main.py", "--port", "8000"]
