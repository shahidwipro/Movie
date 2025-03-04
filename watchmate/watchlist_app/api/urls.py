from django.urls import path 
from watchlist_app.api.serializers import MovieSerializer
#from watchlist_app.api.views import movie_list , movie_details
from watchlist_app.api.views import MovieListAV , MovieDetailsAV 


urlpatterns = [
    
    path('list/', MovieListAV.as_view()),
    path('<int:pk>', MovieDetailsAV.as_view( ))
]
