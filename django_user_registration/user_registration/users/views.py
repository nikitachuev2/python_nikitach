from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def user_list(request):
       users = User.objects.all()
       return render(request, 'users/user_list.html', {'users': users})

def register_user(request):
       if request.method == 'POST':
           form = UserForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('user_list')
       else:
           form = UserForm()
       return render(request, 'users/register_user.html', {'form': form})

def delete_user(request, user_id):
       user = User.objects.get(id=user_id)
       user.delete()
       return redirect('user_list')