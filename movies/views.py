from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_POST
from .models import Movie, MovieComment, Genre
from .forms import MovieCommentForm
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerialzier
import requests
import json
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
def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')


@require_POST
def create(request, movie_id):
    URL_Base ='https://api.themoviedb.org/3'
    path = '/movie/' + str(movie_id)
    params = {
        'api_key' : 'a5bef88bf2657963202297703c0dd532',
        'language' : 'ko-KR',
    }
    response = requests.get(URL_Base+path, params=params).json()
    poster_path = 'https://www.themoviedb.org/t/p/w600_and_h900_bestv2' + response.get('poster_path')
    movie = Movie.objects.create(
        movie_id = response.get('id'),
        title = response.get('title'),
        release_date = response.get('release_date'),
        popularity = response.get('popularity'),
        vote_average = response.get('vote_average'),
        vote_count = response.get('vote_count'),
        overview = response.get('overview'),
        poster_path = poster_path,
        )
    for genre in response.get('genres'):
        movie.genres.add(genre.get('id'))
    
    return redirect('movies:index')


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


def recommended(request):
    user = request.user
    movies = Movie.objects.filter(like_users=user.pk)
    movies_all = Movie.objects.all()
    genres = []
    for movie in movies:
        for genre in movie.genres.all():
            genres.append(genre.id)
    
    context = {
        'movies' : movies,
        'movies_js' : json.dumps([movie.to_json() for movie in movies]),
        'genres' : genres,
        'movies_all_js' : json.dumps([movie.to_json() for movie in movies_all]),
    }
    return render(request, 'movies/recommended.html',context)


@api_view(['GET'])
def recommended_vote(request):
    URL_Base ='https://api.themoviedb.org/3'
    path = '/movie/top_rated'
    params = {
            'api_key' : 'a5bef88bf2657963202297703c0dd532',
            'language' : 'ko-KR',
            'region' : 'KR',
        }
    responses = requests.get(URL_Base+path, params=params).json()
    return Response(responses)


@api_view(['GET'])
def recommended_popularity(request):
    URL_Base ='https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
            'api_key' : 'a5bef88bf2657963202297703c0dd532',
            'language' : 'ko-KR',
            'region' : 'KR',
        }
    responses = requests.get(URL_Base+path, params=params).json()
    return Response(responses)


@api_view(['GET'])
def recommended_now_playing(request):
    URL_Base ='https://api.themoviedb.org/3'
    path = '/movie/now_playing'
    params = {
            'api_key' : 'a5bef88bf2657963202297703c0dd532',
            'language' : 'ko-KR',
            'region' : 'KR',
        }
    responses = requests.get(URL_Base+path, params=params).json()
    return Response(responses)


@api_view(['GET'])
def recommended_upcoming(request):
    URL_Base ='https://api.themoviedb.org/3'
    path = '/movie/upcoming'
    params = {
            'api_key' : 'a5bef88bf2657963202297703c0dd532',
            'language' : 'ko-KR',
            'region' : 'KR',
        }
    responses = requests.get(URL_Base+path, params=params).json()
    return Response(responses)


@api_view(['GET'])
def recommended_my(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    movies = genre.movie_set.order_by('-vote_count')[:10]
    serializer = MovieSerialzier(movies, many=True)
    return Response(serializer.data)


def search(request, keyword):
    movies = Movie.objects.all()
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
        'movies_js' : json.dumps([movie.to_json() for movie in movies]),
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


@api_view(['GET'])
def get_name(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    return Response(genre.name)