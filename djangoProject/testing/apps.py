from django.apps import AppConfig


class TestingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testing'
    verbose_name = '测试平台'



