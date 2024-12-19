from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.db import IntegrityError
from .models import Signup

# Create your views here.


class About(View):
    def get(self, request):
        return render(request, 'about/about.html')

    def post(self, request):
        email = request.POST['email']
        name = request.POST['fname']
   
        try:
            Signup.objects.create(fname=name, email=email).save()
        except IntegrityError as e:
            messages.error(self.request, "Email address already registered.")
            return render(request, 'about/about.html')

        return render(request, 'about/signup_success.html', {'fname': name})
