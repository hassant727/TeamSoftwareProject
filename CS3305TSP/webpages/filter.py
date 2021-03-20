import django_filters
from . models import *

class postFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = (
            'address_line_1',
            'address_line_2',
            'city',
            'county',
            'property_type',
            'number_of_bedrooms',
            'number_of_bathrooms',
            'property_description',
            'price',
            'size',
            'energy_rating',
            'estimated_price',
        )


    # def my_custom_filter(self, queryset, name, value):
    #     return Location.objects.filter(
    #         Q(address_line_1__icontains=value)
    #         | Q(address_line_2__icontains=value)
    #         | Q(city__icontains=value)
    #         | Q(county__icontains=value)
    #         | Q(property_type__icontains=value)
    #         | Q(number_of_bedrooms__icontains=value)
    #         | Q(number_of_bathrooms__icontains=value)
    #         | Q(property_description__icontains=value)
    #         | Q(price__icontains=value)
    #         | Q(energy_rating__icontains=value)
    #         | Q(estimated_price=value)
    #     )