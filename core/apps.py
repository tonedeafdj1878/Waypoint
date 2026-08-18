from django.apps import AppConfig
from django.template.context import Context

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        # Python 3.14 compatibility fix for Django test template context copying
        def patched_copy(self):
            duplicate = Context()
            duplicate.dicts = self.dicts[:]
            return duplicate
        Context.__copy__ = patched_copy