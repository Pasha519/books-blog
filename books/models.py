from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="category/",blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_details", args=[self.id])
    
    

class Post(models.Model):
    STATUS = (('draft','Draft'),('published','Published'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="post",null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300,unique_for_date='publish')
    image = models.ImageField(upload_to="books",blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30,choices=STATUS,default='draft')
    tags = TaggableManager()

    class Meta:
        ordering = ('publish',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_details", args=[self.id])
    
class Review(models.Model):
    STATUS = ((5,5),
    (4,4),
    (3,3),
    (2,2),
    (1,1))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name="review")
    content = models.TextField(default="")
    rating = models.IntegerField(default=1,choices=STATUS)
    created = models.DateTimeField(default=timezone.now)
    
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True,null=True)
    email = models.EmailField()
    desc = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    
    

