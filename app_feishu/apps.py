from django.apps import AppConfig


class AppFeishuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_feishu'

    def ready(self):
        print("[APP Feishu] Ready.")
