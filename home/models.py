from django.db import models
from django.utils.text import slugify
from users.models import Profile


# Create your models here.
class Product(models.Model):

    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True,)
    product_code = models.CharField(unique=True,max_length=220)
    product_name = models.CharField(max_length=200,unique=True)
    description = models.TextField(blank=True,null=True)
    CATEGORY_LIST=(
        ('SHOE','SHOE'),
        ('T-SHIRT','T-SHIRT'),
        ('SHORT','SHORT')
    )
    category = models.CharField(
        max_length=200,
        choices = CATEGORY_LIST,
        default='SHOE',
        blank=True,
        null=True,
    )
    image=models.ImageField(upload_to='home/static/home/img/upload',blank=True,null=True)
    color = models.CharField(max_length=200,blank=True,null=True,)
    size = models.IntegerField(blank=True,null=True)
    quantity = models.IntegerField(blank=True,null=True)
    create = models.DateTimeField(auto_now_add=True,blank=True,null=True,editable=False)
    update =models.DateTimeField(auto_now=True,blank=True,null=True,editable=False)
    slug = models.SlugField(blank=True,null=True,editable=False)
    

    def __str__(self):
        return "{}. {}".format(self.id,self.product_name)

    def save(self):
        self.slug =slugify(self.product_name)
        super(Product,self).save()
