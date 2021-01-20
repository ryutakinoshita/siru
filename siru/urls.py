from django.urls import path
from.import views



urlpatterns = [

    path('set/', views.SetViews.as_view(), name='set'),

]