from django.shortcuts import render
from .forms import WebsiteForm
from .models import ScrapedData
from bs4 import BeautifulSoup
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

def order_submit(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            website_url = form.cleaned_data['website_url']
            response = requests.get(website_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a'):
                url = link.get('href')
                if url and ('http://' in url or 'https://' in url):
                    ScrapedData.objects.create(date_time=datetime.datetime.now(), url=url)
    else:
        form = WebsiteForm()
    return render(request, 'scrape_website.html', {'form': form})