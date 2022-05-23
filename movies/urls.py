from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/comments/create', views.create_comment, name='create_comment'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete', views.delete_comment, name='delete_comment'),
    path('<int:movie_pk>/like', views.like, name='like'),
    path('recommend', views.recommend, name="recommend"),
    path('recommended/vote/', views.recommended_vote, name='recommended_vote'),
    path('recommended/popularity/', views.recommended_popularity, name='recommended_popularity'),
    path('recommended/releasedate/', views.recommended_releasedate, name='recommended_releasedate'),
    path('search/index/<str:keyword>', views.search, name='search'),
    path('search/detail/<int:movie_id>', views.search_detail, name='search_detail'),
]