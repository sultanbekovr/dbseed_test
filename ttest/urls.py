from django.urls import path, include
from . import views

urlpatterns = [
    path('emplist', views.EmployeeView.as_view()),
    path('search/', views.SearchView.as_view()),
    path('filter/', views.FilterView.as_view()),
    path('crud/', views.EmployeeViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('crud/<int:pk>/', views.EmployeeViewSet.as_view(
        {'put': 'update', 'delete': 'destroy'}
    )),


    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
]