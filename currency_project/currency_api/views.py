from rest_framework.views import APIView
from rest_framework import status
from .models import CurrencyRate
from .serializers import CurrencyRateSerializer
import requests
from django.http import JsonResponse
from time import sleep

# ...

class GetCurrentUSD(APIView):
    def get(self, request):
        # Пауза между запросами
        sleep(10)

        # Замените 'YOUR_API_KEY' на ваш API ключ от exchangeratesapi.io
        api_key = 'dae37c9fc8114f0acb3fa375'
        base_url = f'https://open.er-api.com/v6/latest?base=USD&symbols=RUB&apikey={api_key}'

        # Запрос актуального курса доллара к рублю
        response = requests.get(base_url)

        if response.status_code == 200:
            rate = response.json()['rates']['RUB']
            currency_rate = CurrencyRate(rate=rate)
            currency_rate.save()

            # Получение и отображение последних 10 запросов
            last_10_rates = CurrencyRate.objects.order_by('-timestamp')[:10]
            serializer = CurrencyRateSerializer(last_10_rates, many=True)

            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({'error': 'Unable to fetch currency rate'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
