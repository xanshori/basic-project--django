from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('data/',views.data,name='data'),
    path('update/<str:updateinput>/',views.dataupdate,name='update'),
    path('delete/<str:deleteinput>/',views.datadelete,name='delete'),
    path('detail/<slug:detailinput>/',views.detail,name='detail'),
    path('category/<str:categoryinput>/',views.category,name='category'),
    path('export_excel/',views.export_excel,name='export_excel'),

]
