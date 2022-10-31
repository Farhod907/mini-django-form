from django.urls import path
from .views import Main, Royxat
urlpatterns = [
	path('', Main , name='main'),
	path('royxat/', Royxat, name='royxat'),
]