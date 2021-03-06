"""qzzo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from home.views import home, login_page, signup_page, login, signup, user_home_page, update, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login/', login_page, name="login_page"),
    path('signup/', signup_page, name="signup_page"),
    path('user_login/', login, name="login"),
    path('user_signup', signup, name="signup"),
    path('user_home_page/<int:id>', user_home_page, name="user_home_page"),
    path('update_profile/<int:id>/', update, name="update"),
    path('logout/', logout_user, name="logout"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


