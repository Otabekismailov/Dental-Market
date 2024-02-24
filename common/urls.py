from django.urls import path

from common import views

urlpatterns = [
    path('', views.home, name='index'),
    path('create/', views.form_create, name='create'),
    path('404/', views.page_not_found_view, name='page_not_found')
]


