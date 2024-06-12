from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import OrderData
from .forms import OrderDataForm
import requests
import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def pricing(request):
    return render(request, 'partials/pricing.html')

def productinfo(request):
    return render(request, 'partials/productinfo.html')

def faqs(request):
    return render(request, 'partials/faqs.html')

def about(request):
    return render(request, 'partials/about.html')

def order(request):
 return render(request, 'partials/order.html')

def small_order(request):
    if request.method == 'POST':
        form = OrderDataForm(request.POST)
        if form.is_valid():
            form.field_order = ['responsibleParty', 'email', 'phone', 'cases', 'address1', 'address2', 'city', 'state', 'comments']
            return HttpResponseRedirect('/thankyou')
    else:
            form = OrderDataForm()

    return render(request, 'partials/small_order.html', {'form': form})

def med_order(request):
    if request.method == 'POST':
        form = OrderDataForm(request.POST)
        if form.is_valid():
            form.field_order = ['responsibleParty', 'email', 'phone', 'cases', 'address1', 'address2', 'city', 'state', 'comments']
            return HttpResponseRedirect('/thankyou')
    else:
            form = OrderDataForm()

    return render(request, 'partials/med_order.html', {'form': form})

def ent_order(request):
    if request.method == 'POST':
            form = OrderDataForm(request.POST)
            if form.is_valid():
                form.field_order = ['responsibleParty', 'email', 'phone', 'cases', 'address1', 'address2', 'city', 'state', 'comments']
                return HttpResponseRedirect('/thankyou')
    else:
            form = OrderDataForm()

    return render(request, 'partials/ent_order.html', {'form': form})

def thankyou(request):
    entOrderData = request.GET
    return render(request, 'partials/thankyou.html', {'entOrderData': entOrderData})

# class thankyou(TemplateView):
#     template_name = 'partials/thankyou.html'

#     def post(self, request):
#         form = OrderDataForm(request.POST)
#         entFormData = {}
#         if form.is_valid():
#             entFormData = form.cleaned_data("post")

#         args = {'form': form, "context": entFormData}
#         return render(request, self.template_name, args)
