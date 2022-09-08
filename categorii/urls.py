from django.urls import path
from . import views

urlpatterns = [
     
   
      path('', views.PLaces, name='placesy'),
      path('re/', views.regist,  name='reg'),
      path('kontact/', views.kontact, name='kontact-htmm' ),
      path('auth/', views.autenticate, name='authen'),
      path('shop/create/',views.Create_plase, name='create-place'),
      path('shop/<int:id>/', views.detail_post, name='place'),
      path('shop/<int:id>/edit/', views.edit_place, name='edit-place'),
      path('<int:id>/delete/', views.delete_place, name='del_place' ),
     


#       path('feed/', Feedbackcreate.as_view(), name='Feedback'),
#       path('feed/<int:pk>/', FeedbackDetailview.as_view(), name='place'),
    
      
        ]