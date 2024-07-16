from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.ContactFormList.as_view(), name='contact-form-list'),
    path('contact/create/', views.ContactFormCreate.as_view(), name='contact-form-create'),
    path('contact/update/<uuid:edit_token>/', views.ContactFormUpdate.as_view(), name='contact-form-update'),  
]