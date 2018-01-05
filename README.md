# celery-counter
A sample celery application


docker build -t gcr.io/your-project/celery-counter .
gcloud docker -- push gcr.io/your-project/celery-counter


helm upgrade -i counter --set image.repository=gcr.io/your-project/celery-counter charts/counter