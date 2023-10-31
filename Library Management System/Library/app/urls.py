from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('',views.home),
    path('addbook/',views.addbook), 
    path('allbook/',views.allbook),
    path('add/',views.view), #viewname def path 
    path("edit-book/",views.editbookview),
    path("edit-book/edit/",views.editbook),
    path("delete-book",views.deletebookview),

]