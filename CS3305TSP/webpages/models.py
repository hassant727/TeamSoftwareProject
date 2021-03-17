from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from .price_predictor import predict



"""
    run the following code to see what sql query the migration will run python 
    manage.py sqlmigrate name_of_app (folder name in our case blog) sequence number 
    created in migration python manage.py sqlmigrate name_of_app 0001 --> for our case 
"""

COUNTY_CHOICES = [
    ('Antrim', 'Antrim'),
    ('Armagh', 'Armagh'),
    ('Carlow', 'Carlow'),
    ('Cavan', 'Cavan'),
    ('Clare', 'Clare'),
    ('Cork', 'Cork'),
    ('Donegal', 'Donegal'),
    ('Down', 'Down'),
    ('Dublin', 'Dublin'),
    ('Fermanagh', 'Fermanagh'),
    ('Galway', 'Galway'),
    ('Kerry', 'Kerry'),
    ('Kildare', 'Kildare'),
    ('Kilkenny', 'Kilkenny'),
    ('Laois', 'Laois'),
    ('Leitrim', 'Leitrim'),
    ('Limerick', 'Limerick'),
    ('Londonderry', 'Londonderry'),
    ('Longford', 'Longford'),
    ('Louth', 'Louth'),
    ('Mayo', 'Mayo'),
    ('Meath', 'Meath'),
    ('Monaghan', 'Monaghan'),
    ('Offaly', 'Offaly'),
    ('Roscommon', 'Roscommon'),
    ('Sligo', 'Sligo'),
    ('Tipperary', 'Tipperary'),
    ('Tyrone', 'Tyrone'),
    ('Waterford', 'Waterford'),
    ('Westmeath', 'Westmeath'),
    ('Wexford', 'Wexford'),
    ('Wicklow', 'Wicklow'),
]


PROPERTY_TYPE_CHOICES = [
    ('Detached House', 'Detached House'),
    ('Semi-detached House', 'Semi-detached House'),
    ('Terraced House', 'Terraced House'),
    ('Duplex', 'Duplex'),
]

ENERGY_RATING_CHOICES = (
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
    ('G', 'G')
)

energy_rating_dict = {'A1': 15,
                      'A2': 14,
                      'A3': 13,
                      'B1': 12,
                      'B2': 11,
                      'B3': 10,
                      'C1': 9,
                      'C2': 8,
                      'C3': 7,
                      'D1': 6,
                      'D2': 5,
                      'E1': 4,
                      'E2': 3,
                      'F': 2,
                      'G': 1
                      }

property_type_dict = {'Detached House': 1,
                      'Semi-detached House': 2,
                      'Terraced House': 3,
                      'Duplex': 4
                      }


def get_image_filename(instance, filename):
    """
        returns the path that contains the address of the post for the image
    """
    post = instance.post
    address = "-".join(item for item in [post.address_line_1, post.address_line_2, post.city, post.county] if item)
    slug = slugify(address)
    return "post_images/%s-%s" % (slug, filename)



def price_pridiction_model(number_of_bedrooms, number_of_bathrooms, size, property_type, energy_rating):
    """
        the below takes in all the parameter needed for the price prediction and
        returns the estimated price
    """
    attributes = [[number_of_bedrooms, number_of_bathrooms, size, property_type, energy_rating]]
    estimated_price = predict(attributes)
    return estimated_price


class Post(models.Model):
    """
        this code creates a migrations, takes in the class below and creates an sql
        query
        the fields are defined below come teh model defined above
    """
    property_description = models.TextField(null=True, blank=True)
    address_line_1 = models.CharField(max_length=255, verbose_name="Street address")
    address_line_2 = models.CharField(max_length=255, null=True, blank=True, verbose_name="District or Townland")
    city = models.CharField(max_length=128, default='', verbose_name="City or town")
    county = models.CharField(max_length=128, default='', choices=COUNTY_CHOICES)
    floor_plan = models.ImageField(upload_to="floor_plan", null=True, blank=True)
    property_type = models.CharField(max_length=128, default='',
                                     choices=PROPERTY_TYPE_CHOICES)
    number_of_bedrooms = models.PositiveIntegerField()
    number_of_bathrooms = models.PositiveIntegerField()
    energy_rating = models.CharField(max_length=128, default='',
                                     choices=ENERGY_RATING_CHOICES)
    size = models.PositiveIntegerField(verbose_name="Size (m<sup>2</sup>)")
    date_posted = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, related_name="user_posts", on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True, blank=True, editable=True, verbose_name="Price (&euro;)")
    estimated_price = models.PositiveIntegerField(null=False, blank=True, editable=False)
    __original_price = None
    address = models.CharField(max_length=766, null=False, blank=True, editable=False)

    def __str__(self):
        """
            returns the address of a post
        """
        return self.address

    def get_absolute_url(self):
        """
            this method return a string to redirect the user after posting to that
            post by returning post details the primary key of the newly created
            post

            the pk is used to identify each post, meaning when each post is creted,
            it's assigned a pk number :return:
        """
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        """
            overwriting the django save method
            by passing in the estimated price into the price before it is saved
        """
        estimated_price = price_pridiction_model(
            self.number_of_bedrooms,
            self.number_of_bathrooms,
            self.size,
            int(property_type_dict[self.property_type]),
            int(energy_rating_dict[self.energy_rating])
        )
        self.estimated_price = estimated_price
        address = ""
        address_list = [self.address_line_1, self.address_line_2, self.city, self.county]
        for i in range(4):
            if address_list[i] is not None:
                address = address + address_list[i]
                if i < 3:
                    address = address + ", "
        self.address = address
        super().save(force_insert, force_update, *args, **kwargs)


class PostImage(models.Model):
    """
        the model is useed for image posting and image deletion
    """
    image = models.ImageField('images', upload_to=get_image_filename, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='post_images', on_delete=models.CASCADE)

    def delete(self):
        """delete the file when the object is deleted"""
        self.image.delete()
        super(PostImage, self).delete()
