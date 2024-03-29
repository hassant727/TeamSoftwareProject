from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """
        the following is profile model, is used for sizing up the image, setting default profile image when a user is
        created if no image is given and creating the user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """
            resizing the images upload to avoid the images slowing down the response time
        """
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


# """chart modeling"""
#
#
# class Meter(models.Model):
#     """the variables below are the keys in the json dictionary """
#     date = models.DateField()
#     name = models.CharField(max_length=255)
#     reading = models.IntegerField()
#
#     """ordering from latest to oldest"""
#
#     class Meta:
#         ordering = ("-date", "name")
