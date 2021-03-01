from django.db import models

PROPERTY_TYPE_CHOICES = [
    [1, 'Detached House'],
    [2, 'Semi-detached House'],
    [4, 'Terraced House'],
    [3, 'Duplex'],
]

ENERGY_RATING_CHOICES = (
    (15, 'A1'),
    (14, 'A2'),
    (13, 'A3'),
    (12, 'B1'),
    (11, 'B2'),
    (10, 'B3'),
    (9, 'C1'),
    (8, 'C2'),
    (7, 'C3'),
    (6, 'D1'),
    (5, 'D2'),
    (4, 'E1'),
    (3, 'E2'),
    (2, 'F'),
    (1, 'G')
)

class Userdata(models.Model):
    title = models.CharField(max_length=256)
    property_type = models.IntegerField(choices=PROPERTY_TYPE_CHOICES)
    size = models.IntegerField()
    number_rooms = models.IntegerField()
    number_bathrooms = models.IntegerField()
    energy_rating = models.IntegerField(choices=ENERGY_RATING_CHOICES)

