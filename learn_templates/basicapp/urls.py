from django.urls import path
from basicapp import views

#For TEMPLATE TAGGING create a global app_name variable and set to the name of the app
app_name = 'basicapp'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]
