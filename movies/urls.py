from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/comments/create', views.create_comment, name='create_comment'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete', views.delete_comment, name='delete_comment'),
    path('<int:movie_pk>/like', views.like, name='like'),
]