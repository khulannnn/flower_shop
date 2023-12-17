from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    def __str__ (self):
        return self.category_name

class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/subcategory', blank=True)
    def __str__ (self):
        return self.subcategory_name

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.product_name

class Usertype(models.Model):
    usertypename = models.CharField(max_length=50, unique=True)
    def __str__ (self):
        return self.usertypename
    class Meta:
        db_table = 'usertype'
class CustomUserManager(BaseUserManager):
    def create_user(self, username, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('The Phone Number field must be set')
        user = self.model(
            username=username,
            phone_number=phone_number,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, phone_number, password, **extra_fields)
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    phonenumber = models.IntegerField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=False) 
    usertypeid =  models.ForeignKey(Usertype, on_delete=models.CASCADE)
    def __str__ (self):
        return self.username
    class Meta:
        db_table = 'user'


# class Cart_item(models.Model):
#     userid
#     productid
#     size
#     color
#     price
#     count
#     def __str__ (self):