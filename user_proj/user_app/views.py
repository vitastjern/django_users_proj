from django.shortcuts import render
from django.http import request, HttpResponse
from .models import User

# Create your views here.

def index(request):
    my_dict = {'index_title': "Welcome!", 'index_cont': "Go to /users to see users info!"}
    return render(request, 'user_app/index.html', context=my_dict)


def users(request):
    all_users = {'all_users': User.objects.all()}
    print(all_users)
    return render(request, 'user_app/users.html', context = all_users)
   
