from django.urls import path
from .views import user_list, register_user, delete_user

urlpatterns = [
       path('', user_list, name='user_list'),
       path('register/', register_user, name='register_user'),
       path('delete/<int:user_id>/', delete_user, name='delete_user'),
   ]