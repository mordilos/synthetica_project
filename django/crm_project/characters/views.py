from django.http.response import JsonResponse
from rest_framework import generics
from . import models


from .models import Character
from .serializers import CharacterSerializer

# views

# get all the characters 
class CharactersList(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

# function to convert from character object to dictionary 
def characterToDictionary(character):
    output = {}
    output["name"] = character.name
    output["heiht"] = character.height
    output["homeworld"] = character.homeworld
    output["films"] = character.films
    output["url"] = character.url
    return output

# function to return the filtered characters in json format using the above characterToDictionary function
def myView(request, film):
    search_text = '/films/' + film + '/'
    characters = models.Character.objects.all()
    characters_dic = []
    for i in range(len(characters)):
        characters_dic.append(characterToDictionary(characters[i]))

    filtered_characters = []
    for character in characters_dic:
        for film in character['films']:
            if search_text in film:
                filtered_characters.append(character)
    print(filtered_characters)
    return JsonResponse(filtered_characters, safe=False)

# function to return the filtered characters in json format using lambda expressions  
def filter_by_film(request, film):
    search_text = '/films/' + film + '/'

    all_characters_qs = Character.objects.values()

    list_characters = [entry for entry in all_characters_qs]

    filtered_characters = []
    for character in list_characters:
        for films in character['films']:
            if(search_text in films):
                filtered_characters.append(character) 
    

    return JsonResponse(filtered_characters, safe=False)

 
    

