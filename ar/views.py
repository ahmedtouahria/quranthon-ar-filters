from django.shortcuts import render
from .models import Ayaah
def index(request):
    ayaahs = Ayaah.objects.all()
    ctx = {
        "ayahs":ayaahs
    }
    return render(request, 'index.html', ctx)