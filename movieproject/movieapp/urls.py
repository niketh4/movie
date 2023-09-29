from . import views
from django.urls import path
app_name='movieapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('movielist/<int:movie_id>/',views.detail,name='detail'),
    path('add/',views.addmovie,name='addmovie'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),

]