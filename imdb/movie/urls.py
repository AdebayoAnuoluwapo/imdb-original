from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('list/', views.MovieListView.as_view(), name='movie_list'),
    path('category/<str:category>', views.movies_category, name='movie_category'),
    path('language/<str:lang>', views.MovieLanguage.as_view(), name='movie_language'),
    path('<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),

]
