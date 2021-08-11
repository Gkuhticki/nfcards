from django.shortcuts import render
from .models import Page_user
# Create your views here.
def home(request):

    list_users = Page_user.objects.all


    context = {
        'list_users':list_users
    }
    template = 'index.html'
    return render(request, template, context)

def user_page(request, id):
    get_Page_user = Page_user.objects.get(id=id)
    context = {
        'get_Page_user':get_Page_user
    }

    template = 'user.html'
    return render(request, template, context)