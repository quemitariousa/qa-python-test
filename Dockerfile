FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "./code/app/base.py" ]
