celery -A src.celery_tasks.c_app worker --loglevel=info --pool=solo
celery -A src.celery_tasks.c_app flower --address=127.0.0.1
