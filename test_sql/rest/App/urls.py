from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.test_form, name='test_insert'),
    path('<int:id>/', views.test_form, name='test_update'),
    path('delete/<int:id>/', views.test_delete, name='test_delete'),
    path('list/', views.test_list, name='test_list'),
]