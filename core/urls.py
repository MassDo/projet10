"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include

# Views
from users import views as users_views
from signup import views as signup_views
from autocomplete import views as autocomplete_views

# Forms
from users.forms import UserLoginForm
from search.forms import FoodSearchForm

search_form = FoodSearchForm()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search.urls')),

    path('favorites/', include('favorites.urls')),
    path('product/', include('product.urls')),
    path('account/', include('account.urls')),
    path('legals/', include('legals.urls')),
    path('auto/', include('autocomplete.urls')),

    path('signup/', signup_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html',
        authentication_form=UserLoginForm,
        extra_context={'form_search':search_form,}),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html',
        extra_context={'form_search':search_form}),
        name='logout'
    ),
]
