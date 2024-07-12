from django.urls import path
from .views import RegisterView, CustomObtainAuthToken
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomObtainAuthToken.as_view(), name='login'),
    path('logout/', obtain_auth_token, name='logout'),
]