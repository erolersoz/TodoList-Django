from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)#başlık
    slug = AutoSlugField(populate_from='title',unique=True)
    is_active = models.BooleanField(default=False)#When you cascade, the entire table is deleted.

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse(
            'category_view',
            kwargs={
                "category_slug": self.slug
            }
        )




class Tag(models.Model):
    title = models.CharField(max_length=200)#title
    slug = AutoSlugField(populate_from='title',unique=True)
    is_active = models.BooleanField(default=False)#When you cascade, the entire table is deleted.

    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse(
            'tag_view',
            kwargs={
                "tag_slug": self.slug
            }
        )
    




class Todo(models.Model):
    #Category=models.ForeignKey(Category,on_delete=models.CASCADE)#CASCADE
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)#When you cascade, the entire table is deleted.
    title = models.CharField(max_length=200)#title
    content = models.TextField(blank=True,null=True)#explanation
    is_active = models.BooleanField(default=False)#whether active or not
    created_at = models.DateTimeField(auto_now_add=True)#time
    updated_at = models.DateTimeField(auto_now=True)#time now
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'todo_detail_view',
            kwargs={
                "category_slug": self.category.slug,
                "id": self.pk,
            }
        )

    