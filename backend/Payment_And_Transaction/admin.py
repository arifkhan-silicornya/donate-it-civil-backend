from django.contrib import admin
from .models import *
# Register your models here.

# payment
admin.site.register(PaymentMethod)
admin.site.register(CompanyAccount)