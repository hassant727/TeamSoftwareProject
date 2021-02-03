from django.apps import AppConfig


class UserpagesConfig(AppConfig):
    name = 'userpages'

    def ready(self):
        import signals
        from . import signals