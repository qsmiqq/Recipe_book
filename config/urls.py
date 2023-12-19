from book import views
from profiles import views as profiles_views
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('recipes/', include('book.urls')),
    path('profile/', include('profiles.urls')),
    path('login/', profiles_views.login_user, name='login'),
    path('logout/', profiles_views.logout_user, name='logout'),
    path('register/', profiles_views.register_user, name='register')
]



