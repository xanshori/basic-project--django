from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class Profile(models.Model):
    user                = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    name                = models.CharField(max_length=200,unique=True)
    email               = models.EmailField(max_length=400,null=True,blank=True)
    username            = models.CharField(max_length=200,null=True,blank=True)
    career              = models.CharField(max_length=200,null=True,blank=True)
    bio                 = models.TextField(blank=True,null=True,default="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, ")
    profile_image       = models.ImageField(upload_to='users/static/users/img/upload',
                            null=True,blank=True,default='users/static/users/img/upload/default_profile.png')
    profile_header       = models.ImageField(upload_to='users/static/users/img/upload',
                            null=True,blank=True,default='users/static/users/img/upload/header.jpg')
    sosial_github       = models.CharField(max_length=400,null=True,blank=True)
    sosial_instagram    = models.CharField(max_length=400,null=True,blank=True)
    sosial_facebook     = models.CharField(max_length=400,null=True,blank=True)
    sosial_tiktok       = models.CharField(max_length=400,null=True,blank=True)
    created             = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    slug                = models.SlugField(blank=True,null=True)

    def __str__(self):
        return "{}".format(self.username)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(Profile,self).save(*args, **kwargs)


