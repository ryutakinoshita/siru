from django.urls import path
from.import views


urlpatterns = [

    path('set/', views.SetViews.as_view(), name='set'),
    path('contact/',views.ContactView.as_view(), name='contact_form'),
    path('contact/result/',views.ContactResultView.as_view(), name='contact_result'),

]