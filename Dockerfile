FROM python:3.12-alpine

RUN mkdir app
RUN apk add bind-tools

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . /app

#COPY crontab /etc/cron.d/crontab
#RUN crontab /etc/cron.d/crontab

#CMD ["crond", "-f"]
ENTRYPOINT ["sh", "init.sh"]
