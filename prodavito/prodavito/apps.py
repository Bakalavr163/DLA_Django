from django.apps import AppConfig


class ProdavitoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prodavito'

    def ready(self):
        from . import signals
        