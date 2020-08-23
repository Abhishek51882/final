from django.urls import path
from nbr import views

urlpatterns = [
    path('home/',views.greetings),
    path('home/run/',views.runcode),

]
