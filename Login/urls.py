
from django.urls import path
from . import views


urlpatterns = [
    path('',views.login_page,name = 'loginpage'),
    path('signup/',views.sign_up,name = 'signuppage'),
    path('profile/',views.profile_page,name = 'profilepage'),
    path('logout/',views.logout_page,name = 'logoutpage'),
]
