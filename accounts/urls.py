from django.urls import path
from.import views

urlpatterns = [
        path('user/',views.signup,name='user'),
        path('user/change/page/', views.UserChangeTextView.as_view(), name='user-change-page'),
        path('user/change/', views.UserChangeView.as_view(), name="user-change"),
        path('user/Mypage/<int:pk>/', views.MyPageView.as_view(), name='My-page'),
]