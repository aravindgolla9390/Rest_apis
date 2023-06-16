from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('data/',bookdata,name='bookdata'),
    path('add',addingBookdata,name='addingBookdata'),
    path('update/<int:id>/',updatingBookdata,name='updatingBookdata'),
    path('delete/<int:id>/',deletingBookdata,name='deletingBookdata'),
    
]