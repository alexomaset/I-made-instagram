from django.db import models
from django.http  import HttpResponse

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)#USER Models
	name = models.TextField(max_length=500, blank=True)
	bio = models.TextField(max_length=500, blank=True)
	website = models.CharField(max_length=30,blank=True)
	email = models.EmailField()
	phone_number = PhoneNumberField(max_length=10, blank=True)
	photo = models.ImageField(upload_to = 'profile/',blank=True,default=False)
	gender = models.CharField(max_length=30,choices=Genders_Choices,default='None',blank=True)
	
	def __str__(self):
		return self.user.username
