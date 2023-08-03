from django.urls import path

from rentaldetails import views


urlpatterns = [

    path('', views.index,),
    path('details', views.details, name='details'),
    path('about', views.about, name='about'),
 ]