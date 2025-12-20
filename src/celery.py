import os
from celery import Celery
from celery.schedules import crontab 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

app = Celery('src')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



# app.conf.beat_schedule = {
#     'refresh_recommendations_every_2_days': {
#         'task': 'events.tasks.delete_event.delete_events',  
#         'schedule': crontab(minute=0, hour=12),  
#         'args': (), 
#     },
# }