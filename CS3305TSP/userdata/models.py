from django.db import models

class Userdata(models.Model):
    property_name = models.CharField(max_length=256)
    property_area = models.IntegerField()
    property_index = models.IntegerField()
    property_index2 = models.IntegerField()
    property_index3 = models.IntegerField()
    property_index4 = models.IntegerField()

