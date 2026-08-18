from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('report/', views.report_trail_view, name='report_trail'),
]