from django.shortcuts import render
from .models import User
# Create your views here.
def home(request):

    list_users = User.objects.all


    context = {
        'list_users':list_users
    }
    template = 'index.html'
    return render(request, template, context)
def user_page(request, id):
    get_user = User.objects.get(id=id)
    context = {
        'get_user': get_user
    }

    template = 'user.html'
    return render(request, template, context)