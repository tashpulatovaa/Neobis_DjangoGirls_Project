from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('add', views.create_post, name='add')
]