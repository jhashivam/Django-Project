"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin # Imports the admin module, which provides the Django admin interface for managing the site's data.
from django.urls import path, include # Imports the path and include functions from django.urls. The path function is used to define URL patterns, and the include function allows referencing other URL configurations.
from posts import views # Imports the views module from the posts app. This allows access to the view functions defined in posts/views.py, which handle requests for specific URLs.

urlpatterns = [ #   Defines a list named urlpatterns that contains URL patterns for the blog project. Each pattern maps a URL path to a specific view function or another URL configuration.
    path('admin/', admin.site.urls), # Maps the URL path 'admin/' to the Django admin site. When a user visits this URL, they will be directed to the admin interface.
    path('post/', include('posts.urls')), # Maps the URL path 'post/' to the URL configurations defined in the posts app. The include() function allows you to reference another URLconf, in this case, the one defined in posts/urls.py. This means that any URL starting with 'post/' will be handled by the URL patterns defined in the posts app.
    path('google/', views.google , name='google'),  # Maps the URL path 'google/' to the google view function in views.py. When a user visits this URL, the google view will be executed.
    path('<int:id>/', views.redirect_to_id , name='redirect_to_id'),  # Maps any URL that consists of an integer (e.g., '1/', '2/', etc.) to the redirect_to_id view function in views.py. The integer is captured as a parameter named id and passed to the view function. This allows for dynamic URL handling based on the provided integer.
     path('home/<str:name>/', views.home , name='home'),  # Maps the URL path 'home/<str:name>/' to the home view function in views.py. The <str:name> part captures a string parameter named name from the URL and passes it to the home view function. This allows for dynamic URL handling based on the provided name.
]
