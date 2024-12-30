from django.contrib.auth import get_user_model
from django.shortcuts import render

from accounts.models import Profile


# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            profile = None
    else:
        user = None
        profile = None

    context = {'user': user}

    return render(request, 'common/index.html', context)
