from django.db import models
from django.db.models.fields import CharField
from django.contrib.postgres.fields import ArrayField

# my model for the characters db
class Character(models.Model):
    name = CharField("name", max_length=24, primary_key=True)
    height = CharField("height", max_length=24)
    homeworld = CharField("homeworld", max_length=24)
    films = ArrayField(CharField("films", max_length=24), size = 8)
    url = CharField("url", max_length=240)


    class Meta:
        db_table = 'characters'

    def __str__(self):
        return self.Name

    def get_films(self):
        return self.films

    def get_self(self):
        return [self.name, self.height, self.homeworld, self.films, self.url]


