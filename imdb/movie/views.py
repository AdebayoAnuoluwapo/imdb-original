from django.shortcuts import render
from django.views.generic import (
    ListView, TemplateView, DeleteView, DetailView)
from .models import Movie, MovieLinks, CATEGORY_CHOICES


# Create your views here.


class HomeView(TemplateView):
    template_name = 'movie/index.html'


class MovieListView(ListView):
    context_object_name = 'movies'
    model = Movie
    template_name = 'movie/movie_list.html'
    paginate_by = 2


class MovieDetailView(DetailView):
    model = Movie

    # return only one movie
    def get_object(self):
        object = super(MovieDetailView, self).get_object()
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self, *args, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        return context


# class MovieCategory(ListView):
#     model = Movie
#     paginate_by = 2

#     def get_queryset(self, **kwargs):
#         self.category = self.kwargs['category']
#         return Movie.objects.filter(category=self.category)

#     def get_context_data(self, **kwargs):
#         context = super(MovieCategory, self).get_context_data(**kwargs)
#         context['movie_category'] = self.category
#         return context


def movies_category(request, category):
    movies = Movie.objects.filter(category=category)
    context = {
        'movies': movies,
        'movie_category': category,
    }
    return render(request, 'movie/movie_list.html', context)


class MovieLanguage(ListView):
    model = Movie
    paginate_by = 1

    def get_queryset(self, **kwargs):
        self.language = self.kwargs['lang']
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context
