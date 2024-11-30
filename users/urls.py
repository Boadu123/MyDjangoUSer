from django.urls import path
from .views import UserView, logout_view, register_view
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', register_view, name='register'),
    path('users/', UserView.as_view(), name='get_users'),
    path('users/<uuid:id>/', UserView.as_view(), name='user_detail'),
    path('users/update/<uuid:id>/', UserView.as_view(), name='update_user'),
    path('users/partial-update/<uuid:id>/', UserView.as_view(), name='partial_update_user'),
    path('users/delete/<uuid:id>/', UserView.as_view(), name='delete_user'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout_view, name='logout'),

]
