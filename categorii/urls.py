from django.urls import path
from . import views

urlpatterns = [
      path('', views.PLaces, name='placesy'),
      path('re/', views.regist,  name='reg'),
      path('kontact/', views.kontact, name='kontact-htmm' ),
      path('auth/', views.autenticate, name='authen'),
      path('plase/create/',views.Create_plase, name='create-place'),
      path('plase/<int:id>/', views.detail_post, name='place'),
      path('plase/<int:id>/edit/', views.edit_place, name='edit-place'),
      path('by/', views.bu_htm, name='by-project'),
      path('<int:id>/delete/', views.delete_place, name='del_place' ),


#       path('feed/', Feedbackcreate.as_view(), name='Feedback'),
#       path('feed/<int:pk>/', FeedbackDetailview.as_view(), name='place'),
    
      
        ]