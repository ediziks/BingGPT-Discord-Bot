FROM python:3.12.2-slim-bullseye

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "python3", "src/bot.py" ]
