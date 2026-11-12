from django.urls import path
from posts import views

urlpatterns = [
    # path('helloworld', views.helloworld)
    path('home/', views.home),# Maps the root URL (i.e., the homepage) to the home view function in views.py. When a user visits the base URL of the site, the home view will be executed.
    path('<int:id>/', views.post)
]