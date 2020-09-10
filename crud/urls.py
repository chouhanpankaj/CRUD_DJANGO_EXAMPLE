from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentListView.as_view(), name='list'),
    path('add/', views.StudentCreateView.as_view(), name='add'),
    path('update/<int:pk>', views.StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.StudentDeleteView.as_view(), name='delete'),
]
