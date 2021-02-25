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

PROPERTY_TYPE_CHOICES = [
    ('House', 'House'),
    ('Detached House', 'Detached House'),
    ('Semi-detached House', 'Semi-detached House'),
    ('Terraced House', 'Terraced House'),
    ('End of Terrace House', 'End of Terrace House'),
    ('Townhouse', 'Townhouse'),
    ('Apartment', 'Apartment'),
    ('Studio Apartment', 'Studio Apartment'),
    ('Duplex', 'Duplex'),
    ('Bangalow', 'Bangalow'),
]

ENERGY_RATING_CHOICES = [
    ('Exempted','Exempted'),
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('A3', 'A3'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('B3', 'B3'),
    ('C1', 'C1'),
    ('C2', 'C2'),
    ('C3', 'C3'),
    ('D1', 'D1'),
    ('D2', 'D2'),
    ('E1', 'E1'),
    ('E2', 'E2'),
    ('F', 'F'),
    ('G', 'G'),
]

def get_image_filename(instance, filename):
    post = instance.post
    address = "-".join(item for item in [post.address_line_1, post.address_line_2, post.city, post.county] if item)
    slug = slugify(address)
    return "post_images/%s-%s" % (slug, filename)

class Post(models.Model):
    title = models.CharField(max_length=128, default='')
    property_description = models.TextField(null=True, blank=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=128, default='')
    county = models.CharField(max_length=128, default='')
    floor_plan = models.ImageField(upload_to=get_image_filename, null=True, blank=True)
    property_type = models.CharField(max_length=128, choices=PROPERTY_TYPE_CHOICES)
    number_of_bedrooms = models.PositiveIntegerField()
    number_of_bathrooms = models.PositiveIntegerField()
    price = models.PositiveIntegerField(null=True, blank=True)
    energy_rating = models.CharField(max_length=128, choices=ENERGY_RATING_CHOICES, null=True, blank=True)

    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User,related_name="user_posts", on_delete=models.CASCADE)

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

class PostImage(models.Model):
    image = models.ImageField('images', upload_to=get_image_filename, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)

    def delete(self):
        # delete the file when the object is deleted
        self.image.delete()
        super(PostImage, self).delete()