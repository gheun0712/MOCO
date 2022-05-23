from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_POST
from .models import Movie, MovieComment
from .forms import MovieCommentForm
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerialzier
import requests
# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.order_by('-popularity')
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    comments = MovieComment.objects.filter(movie_id=movie.pk)
    comment_form = MovieCommentForm()
    context = {
        'movie' : movie,
        'comments' : comments,
        'comment_form':comment_form,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def create_comment(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)

    comments = MovieComment.objects.filter(movie_id=movie.pk)
    user_list = []
    for comment in comments:
        user_list.append(comment.user_id)

    if request.user.pk in user_list:
        messages.warning(request, "한줄평은 영화당 하나씩 작성할 수 있습니다.")
    else:
        comment_form = MovieCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
    return redirect('movies:detail', movie.pk)


@require_POST
def delete_comment(request,movie_pk, comment_pk):
    movie = Movie.objects.get(pk=movie_pk)
    comment = MovieComment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie.pk)


def like(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    user = request.user

    if user in movie.like_users.all():
        movie.like_users.remove(user)
    else :
        movie.like_users.add(user)
    count = movie.like_users.count()
    return JsonResponse({'count':count})


def recommend(request):
    return render(request, 'movies/recommend.html')


@api_view(['GET'])
def recommended_vote(request):
    movies = Movie.objects.order_by('-vote_average')[:10]
    serializer = MovieSerialzier(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recommended_popularity(request):
    movies = Movie.objects.order_by('-popularity')[:10]
    serializer = MovieSerialzier(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recommended_releasedate(request):
    movies = Movie.objects.order_by('-release_date')[:10]
    serializer = MovieSerialzier(movies, many=True)
    return Response(serializer.data)


def search(request, keyword):
    URL_Base ='https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
            'api_key' : 'a5bef88bf2657963202297703c0dd532',
            'query' : keyword,
            'language' : 'ko-KR',
            'region' : 'KR',
        }
    responses = requests.get(URL_Base+path, params=params).json()
    context = {
        'responses': responses,
        'keyword' : keyword,
    }
    return render(request, 'movies/search.html', context)


def search_detail(request, movie_id):
    URL_Base ='https://api.themoviedb.org/3'
    path = '/movie/' + str(movie_id)
    params = {
        'api_key' : 'a5bef88bf2657963202297703c0dd532',
        'language' : 'ko-KR',
    }
    response = requests.get(URL_Base+path, params=params).json()
    context = {
        'response' : response
    }
    return render(request, 'movies/search_detail.html', context)
