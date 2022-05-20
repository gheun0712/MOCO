from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_POST
from .models import Movie, MovieComment
from .forms import MovieCommentForm
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