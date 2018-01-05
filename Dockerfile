FROM python:3

RUN pip install celery 

COPY src/* /

CMD ["/usr/local/bin/celery", "-A", "tasks", "worker", "--loglevel=info"]

