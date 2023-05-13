from django.apps import AppConfig



class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        from api.scrape.backgroud_schduler import start
        start()

