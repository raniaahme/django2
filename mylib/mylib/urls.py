from django.contrib import admin
from django.urls import path
from catagory import views
from book import views as bookviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.List,name='Catagory_List'),
    path('Book/Add',bookviews.Add,name='Book_Add'),
    path('Catatory/Add',views.Add,name='Catagory_Add'),
    path('Catatory/Update/<int:catid>',views.Update,name='Catagory_Update'),
    path('booklist',bookviews.List,name='Book_List'),

]
