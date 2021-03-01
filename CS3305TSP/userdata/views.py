from django.shortcuts import render
from django.views import View
from .forms import UserdataModelForm
from django.http import JsonResponse
from .price_predictor import predict


# Create your views here.

class UserdatFucntionView(View):
    form = UserdataModelForm()

    def get(self, request):
        form = UserdataModelForm()
        return render(request, 'userdata/userdata.html', {'form':form})

    def post(self, request):
        if request.method == "POST":
            form = UserdataModelForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                form.save()

                no_rooms = data["number_rooms"]
                no_bathrooms = data["number_bathrooms"]
                size = data["size"]
                type = data["property_type"]
                energy_rating = data["energy_rating"]

                attributes = [[no_rooms, no_bathrooms, size, type, energy_rating]]
                print(predict(attributes))
                return JsonResponse(data)

        return render(request, 'userdata/userdata.html', {'form':form})
