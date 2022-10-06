from datetime import datetime


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "DocBlog/index.html", context={"date": datetime.today()})


def test(request): 
    return HttpResponse("Ceci est un test")