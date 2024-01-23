from django.contrib import admin
from django.urls import path, include
from currency_api.views import GetCurrentUSD

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-current-usd/', GetCurrentUSD.as_view(), name='get_current_usd'),
]
