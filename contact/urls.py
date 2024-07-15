from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.ContactFormList.as_view(), name='contact-form-list'),
    path('contact/<int:pk>/', views.ContactFormDetail.as_view(), name='contact-form-detail'),
    path('contact/<int:pk>/final/', views.FinalSubmitContactForm.as_view(), name='final-submit-contact-form'),
]