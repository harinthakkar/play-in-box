from django.urls import path
from.import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    
    path('register/',views.SignUp.as_view(),
         name='register'),

    path('owner_SignUp/',views.owner_SignUp.as_view(),
         name='owner_SignUp'),


    path('login/',auth_views.LoginView.as_view(template_name='login.html'),
         name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
      path('',views.DemoFunction,name="home"),
    path('nishit/',views.Login.as_view(),
        name='index'),
    
    path('viewCategory/',views.viewCategory,name="viewCategory"),
     
    path('view_grounds/',views.view_ground,name="view_ground"), 

    path('addCategory/',views.addCategory,name="addCategory"),
   
    path('deleteCategory/<id>',views.deleteCategory,name="deleteCategory"),
    path('updateCategory/<id>',views.updateCategory,name="updateCategory"),
    path('bulkUpload/',views. bulk_upload,name='bulkUpload'),
    path('upload_csv',views.upload_csv,name='upload_csv'),
    path('download_csv',views.download_csv,name="download_csv"),
    path('add_ground/<id>', views.add_ground, name='add_ground'),
    path('book_ground/<int:user_id>/<int:gid>', views.book_ground, name='book_ground'),
    path('ground_details/<id>', views.ground_details, name='ground_details'),
    path('profile/',views.profile,name="profile"),
]
    