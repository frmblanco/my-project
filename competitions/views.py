from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404


def competitions_list(request):
    comps = Competitions.objects.order_by('-pub_date')
    return render(request, 'competitions/index.html', {'comps': comps})


def competitions_signup(request, pk):
    comps = get_object_or_404(Competitions, pk=pk)
    return render(request, 'competitions/signup.html', {"comps": comps})


def comp_success(request, pk):
    comps = get_object_or_404(Competitions, pk=pk)

    if request.method == 'POST':
        user_id = int(request.user.id)
        user = CustomUser.objects.get(id=user_id)
        post_id = Competitions.objects.get(pk=pk)
        file = request.POST['file']
        entry = CompetitionFile()
        entry.create_row(user, post_id, file)
        entry.save()

    return render(request, 'competitions/comp_success.html', {'comps': comps})
