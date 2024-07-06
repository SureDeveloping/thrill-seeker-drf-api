from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.ContactFormList.as_view(), name='contact-form-list'),
    path('contact/<uuid:edit_token>/', views.ContactFormDetail.as_view(), name='contact-form-detail'),
]