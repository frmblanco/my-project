from django.shortcuts import render
from .models import *


def competitions_list(request):
    comps = Competitions.objects.select_related().order_by('-pub_date')
    return render(request, 'competitions/index.html', {'comps': comps})


def competitions_signup(request, pk):
    comps = Competitions.objects.select_related().get(pk=pk)
    return render(request, 'competitions/signup.html', {"comps": comps})
