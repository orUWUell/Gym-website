FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/dm_rest

COPY ./requirements.txt /usr/src/req.txt
RUN pip install -r /usr/src/req.txt

COPY . /usr/src/dm_rest

EXPOSE 8000

CMD ["python", "python", "runserver", "0.0.0.0:8000"]
