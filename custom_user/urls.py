from django.urls import path

from custom_user.views import authenticate_user, registration_user, user_profile, logout_user

urlpatterns = [
    path('', authenticate_user, name='authenticate'),
    path('reg/', registration_user, name='registration'),
    path('profile/', user_profile, name='profile'),
    path('logout/', logout_user, name='logout_user'),
]
