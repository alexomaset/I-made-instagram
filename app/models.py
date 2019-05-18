from django.db import models
from django.http  import HttpResponse

# Create your models here.
def welcome(request):
    return HttpResponse('IG')