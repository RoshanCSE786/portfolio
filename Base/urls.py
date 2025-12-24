from django.urls import path
from . import views
from .api_views import contact_api

urlpatterns = [
    path('',views.contact),
    path('api/contact/', contact_api, name='contact_api'),
]