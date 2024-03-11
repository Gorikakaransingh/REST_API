from django.urls import path
from restapp import views

urlpatterns = [
   path('client', views.clients), # get (all students) and post both requests
   path('client/<cid>',views.clientDetails), # get (by id), delete n put
#    path('*',views.errorResponse),
]
