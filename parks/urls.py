
from django.urls import path
from parks import views

urlpatterns = [
    path('parks/', views.ParkList.as_view()),
]
