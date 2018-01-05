import time
from celery import Celery

BROKER_URL = [
    'amqp://my_user:my_pass@rmq-0.rmq.default.svc.cluster.local:5672/my_vhost',
    'amqp://my_user:my_pass@rmq-1.rmq.default.svc.cluster.local:5672/my_vhost',
    'amqp://my_user:my_pass@rmq-2.rmq.default.svc.cluster.local:5672/my_vhost',
]
app = Celery('tasks', broker=BROKER_URL)


@app.task
def count():
    for i in range(10):
        print(i)
        time.sleep(1)
