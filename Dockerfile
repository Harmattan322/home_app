FROM python:3.6

RUN mkdir -p /var/applications/home_app
COPY . /var/applications/home_app

WORKDIR /var/applications/home_app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3", "manage.py" ]
