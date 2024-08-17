from django.shortcuts import render
from accounts.models import User

def about_us(request):
    data = User.objects.all()
    context = {
        'users': data
    }
    return render(request, 'about_us.html', context)
