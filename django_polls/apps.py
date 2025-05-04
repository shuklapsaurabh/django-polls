from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_polls'
    label = 'polls' # This label is used to avoid name clashes with other apps
    verbose_name = 'Polls Application' # This is the human-readable name for the app