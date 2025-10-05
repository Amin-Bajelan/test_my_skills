from django.urls import path
from . import views
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView
from django.contrib import admin
from django.urls import path, include



urlpatterns = [

    path('index/', views.index, name='index'),
    # registration
    path('registration/', views.RegistrationApi.as_view(), name='registration'),
    path('token/login/', views.custom_obtain_auth_token.as_view(), name='token_login'),
    path('token/logout/', views.CustomDestroyToken.as_view(), name='token_logout'),
    # change password
    # reset password
    # login token
    # jwt token
    path('jwt/token/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]