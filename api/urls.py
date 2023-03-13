from django.urls import path
app_name = 'api'
from api.views import UserSignInView


urlpatterns = [
    # path('signup', UserRegisterView.as_view(), name='signup'),
    path('login', UserSignInView.as_view(), name='login'),
]
