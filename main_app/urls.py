from django.urls import path
from . import views

urlpatterns = [
  path('', views.wishes_index, name='home'),
  path('wishes/', views.wishes_index, name='index'),
  path('wishes/create/', views.WishCreate.as_view(), name='wishes_create'),
  path('wishes/<int:pk>/delete/', views.WishDelete.as_view(), name='wishes_delete'),
]