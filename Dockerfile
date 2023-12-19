FROM python:3
COPY landingpage /app/landingpage/
COPY requirements.txt /app
COPY manage.py /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 0:8000