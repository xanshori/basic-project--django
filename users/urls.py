from django.urls import path
from .import views


urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('edit/',views.editprofile,name='edit'),
    path('create/',views.createprofile,name='create'),
    path('delete/<int:deleteinput>/',views.deleteprofile,name='delete'),
    path('update/<int:updateinput>/',views.updateprofile,name='update'),
    path('detail/<slug:detailinput>/',views.detailprofile,name='detailprofile'),
    path('',views.userlogin,name='login'),
    path('logout/',views.userlogout,name='logout'),
    path('register/',views.userregister,name='register'),
   
]
