from django.urls import path
from posts import views

urlpatterns = [
    # path('helloworld', views.helloworld)
    path('home/', views.home),
    path('<int:id>/', views.post)
]