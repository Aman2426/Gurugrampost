from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    name=models.CharField('Full Name',max_length=30)
    bio=models.TextField(max_length=300)
    slug=models.SlugField(max_length=60, unique=True)
    img=models.ImageField()
    dob=models.DateTimeField('Date of Birth')

    def __str__(self):
        return self.name
