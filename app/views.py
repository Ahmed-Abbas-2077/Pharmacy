from django.shortcuts import render
from .forms import CreateCustomer
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Customer


def create(request):
    if request.method == "POST":
        form = CreateCustomer(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            first = cd["First_Name"]
            second = cd["Second_Name"]
            customer = Customer(First_Name=first,Second_Name=second)
            customer.save()            
            return HttpResponseRedirect(reverse("create"))
    else:
        form = CreateCustomer()
        return render(request , "app/create.html", {'form':form})