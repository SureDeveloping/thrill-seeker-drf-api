from django.urls import path
from .views import views


urlpatterns = [
    path('contact/', views.ContactFormList.as_view(), name='contact-form-list'),
    path('contact/<int:pk>/', views.ContactFormDetail.as_view(), name='contact-form-detail'),
]