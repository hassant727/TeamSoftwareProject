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
    property_type = models.IntegerField(choices=PROPERTY_TYPE_CHOICES)
    number_of_bedrooms = models.PositiveIntegerField()
    number_of_bathrooms = models.PositiveIntegerField()
    price = models.PositiveIntegerField(null=True, blank=True)
    energy_rating = models.IntegerField(choices=ENERGY_RATING_CHOICES)
    size = models.IntegerField()
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