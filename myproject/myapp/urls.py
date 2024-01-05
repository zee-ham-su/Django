from django.urls import path
from .views import about, submit_data

urlpatterns = [
    path('about/', about, name='about'),
    path('submit/', submit_data, name='submit_data'),
]
