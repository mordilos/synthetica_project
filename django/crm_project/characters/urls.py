from django.urls import include, path
from .views import CharactersList
from . import views

urlpatterns = [
    # show all characters
    path('', CharactersList.as_view()),
    # show characters filtered by film. after the characters page add /films/x/ to show characters that played in the x-th film
    path('films/<str:film>/', views.filter_by_film),
    # this is a different way to show the data needed. if you want you can try it
    # path('films/<str:film>/', views.myView),
]