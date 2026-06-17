from django.apps import AppConfig
from django.conf import settings

class LettersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'letters'

    def ready(self):
        if settings.DEBUG:
            from .scheduler import start_scheduler
            start_scheduler()