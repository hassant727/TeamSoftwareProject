from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
"""this code creates a migrations, takes in the class below and creates an sql query"""

"""run the following code to see what sql query the migration will run 
python manage.py sqlmigrate blog (folder name in our case blog) sequence number created in migration
python manage.py sqlmigrate blog 0001 --> for our case 
"""


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    """
        this method return a string to redirect the user after posting to that post by returning post details the 
        primary key of the newly created post
    """
    def get_absolute_url(self):
        """
        the pk is used to identify each post, meaning when each post is creted, it's assigned a pk number
        :return:
        """
        return reverse('post-detail', kwargs={'pk': self.pk})
