from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_id>/movie/create', views.create, name='create'),
    path('<int:movie_pk>/delete', views.delete, name='delete'),
    path('<int:movie_pk>/comments/create', views.create_comment, name='create_comment'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete', views.delete_comment, name='delete_comment'),
    path('<int:movie_pk>/like', views.like, name='like'),
    path('recommended', views.recommended, name="recommended"),
    path('recommended/vote/', views.recommended_vote, name='recommended_vote'),
    path('recommended/popularity/', views.recommended_popularity, name='recommended_popularity'),
    path('recommended/now_playing/', views.recommended_now_playing, name='recommended_now_playing'),
    path('recommended/upcoming/', views.recommended_upcoming, name='recommended_upcoming'),
    path('recommended/my/<int:genre_id>/', views.recommended_my, name='recommended_my'),
    path('search/index/<str:keyword>', views.search, name='search'),
    path('search/detail/<int:movie_id>', views.search_detail, name='search_detail'),
    path('genre/<int:genre_id>', views.get_name, name='get_name'),
]