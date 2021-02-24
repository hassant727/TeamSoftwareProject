from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .forms import UserdataModelForm
from django.http import JsonResponse



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
                var = JsonResponse(data)
                return JsonResponse(data)

        return render(request, 'userdata/userdata.html', {'form':form})
