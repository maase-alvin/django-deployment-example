from django.urls import path
from appfour import views

# Template tagging
app_name = 'appfour'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/', views.other, name='other'),
]
