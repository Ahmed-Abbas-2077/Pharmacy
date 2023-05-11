from django.contrib import admin

# Register your models here.
from .models import Customer,Customer_Condition,Medication,Dispense
admin.site.register((Customer,Customer_Condition,Medication,Dispense))
