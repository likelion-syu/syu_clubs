FROM python:3

# RUN apt-get update && apt-get -y install \
#     libpq-dev
RUN apt-get -y install \
libpq-dev
WORKDIR /app
ADD    ./requirements.txt   /app/
RUN    pip install -r requirements.txt

ADD    ./djangosample   /app/djangosample/
ADD    ./manage.py      /app/

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0:8000"]
