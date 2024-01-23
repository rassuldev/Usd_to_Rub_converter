from django.db import models

class CurrencyRate(models.Model):
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rate} at {self.timestamp}'
