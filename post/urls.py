from django.urls import path
from .import views

urlpatterns=[
    path('', views.HomeViews.as_view(), name='home'),
    path('create/',views.PostCreateView.as_view(),name='create'),
    path('comment/<int:pk>/',views.CommentView.as_view(),name='comment'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('post/<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),

]