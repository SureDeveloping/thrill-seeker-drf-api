from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.ContactFormCreate.as_view(), name='contact-create'),
    path('contact/<uuid:edit_token>/', views.ContactFormDetail.as_view(), name='contact-detail'),
]