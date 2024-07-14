from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.ContactFormList.as_view(), name='contact-form-list'),
    path('api/contact/final/', FinalSubmitContactForm.as_view(), name='final_submit_contact_form'),
]