
import hashlib
from django.shortcuts import render
from django.http import HttpResponse

from .forms import UrlForm
from .models import Url

def make_short_url(full_url):
    return hashlib.sha224(full_url.encode("utf-8")).hexdigest()[:7]

def index(request):
    short_url = None
    form = UrlForm()
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            full_url = form.cleaned_data['full_url']
            short_url = make_short_url(full_url)

            url = Url()
            url.full_url = full_url
            url.short_url = short_url
            url.save()

    
    context = {
        'form': form,
        'short_url': short_url,
    }
    return render(request, "urlshrt/index.html", context = context)

