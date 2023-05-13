from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ScrapeCryptoCurrencyView, CurrencyRecordViewSet


app_name = "Crypto Currency"

router = DefaultRouter()

router.register("records", CurrencyRecordViewSet,  basename='update')



urlpatterns = [
    path('run-scraper/', ScrapeCryptoCurrencyView.as_view(), name='scrap'),
    # path("", include(router.urls)),
]