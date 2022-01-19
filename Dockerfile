FROM python:3.8

ENV PYTHONUNBUFFERD 1
RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip3 install -r requeriments.txt

CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "admin", "admin.wsgi:application"]
#el puerto se definió en /nginx/local.conf