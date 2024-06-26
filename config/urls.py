"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
<<<<<<< HEAD
from orders.views import OrderListView

urlpatterns = [
    path('', OrderListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', include('users.urls'), name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('orders/', include('orders.urls'), name='orders'),
    path('ratings/', include('ratings.urls'), name='ratings'),
    path('services/', include('services.urls'), name='services'),
    path('executers/', include('executers.urls'), name='executers'),
    path('customers/', include('customers.urls'), name='customers'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
from config.ddtb import DEBUG_TOOLBAR_PATH

from freelance.views import RegisterView

from django.urls import path


urlpatterns = [
    path('', include('freelance.urls')),
    path('ratings/', include('ratings.urls')),
    path('services/', include('services.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #Services
    path("services/", include("services.urls"), name = "services"),

    DEBUG_TOOLBAR_PATH, 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

>>>>>>> ffce688842ec1fa75373b03dbab3af6db23f1b1a
