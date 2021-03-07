from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from .price_predictor import predict

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


"""the below takes in all the parameter needed for the price prediction and returns the estimated price"""


def price_pridiction_model(number_of_bedrooms, number_of_bathrooms, size, property_type, energy_rating):
    attributes = [[number_of_bedrooms, number_of_bathrooms, size, property_type, energy_rating]]
    estimated_price = predict(attributes)
    return estimated_price


class Post(models.Model):
    property_description = models.TextField(null=True, blank=True)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=128, default='')
    county = models.CharField(max_length=128, default='')
    floor_plan = models.ImageField(upload_to="floor_plan", null=True, blank=True)
    property_type = models.IntegerField(choices=PROPERTY_TYPE_CHOICES)
    number_of_bedrooms = models.PositiveIntegerField()
    number_of_bathrooms = models.PositiveIntegerField()
    energy_rating = models.IntegerField(choices=ENERGY_RATING_CHOICES)
    size = models.IntegerField()
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, related_name="user_posts", on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True, blank=True, editable=True)
    __original_price = None

    def __str__(self):
        address = ""
        address_list = [self.address_line_1, self.address_line_2, self.city, self.county]
        for i in range(4):
            address = address + address_list[i]
            if i < 3:
                address = address + ", "
        return address

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

    """
        overwriting the django save method 
        by passing in the estimated price into the price before it is saved
    """

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        estimated_price = price_pridiction_model(
            self.number_of_bedrooms,
            self.number_of_bathrooms,
            self.size,
            self.property_type,
            self.energy_rating
        )
        self.price = estimated_price
        super().save(force_insert, force_update, *args, **kwargs)


class PostImage(models.Model):
    image = models.ImageField('images', upload_to=get_image_filename, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)

    def delete(self):
        """delete the file when the object is deleted"""
        self.image.delete()
        super(PostImage, self).delete()
