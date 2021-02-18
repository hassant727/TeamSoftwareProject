from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
"""this code creates a migrations, takes in the class below and creates an sql query"""

"""run the following code to see what sql query the migration will run 
python manage.py sqlmigrate blog (folder name in our case blog) sequence number created in migration
python manage.py sqlmigrate blog 0001 --> for our case 
"""


class Post(models.Model):
    title = models.CharField(max_length=128)
    property_description = models.TextField()
    address_line_1 = models.CharField(max_length=255, default='')
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=128, default='')
    county = models.CharField(max_length=128, default='')

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

def get_image_filename(instance, filename):
    title = instance.post.title
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class PostImage(models.Model):
    image = models.ImageField('images', upload_to=get_image_filename, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)