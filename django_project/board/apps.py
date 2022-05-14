from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "django_project.board"
    verbose_name = _("Board")
