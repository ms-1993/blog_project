from multiprocessing.synchronize import SemLock

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# each field in this class represents a column in the database table
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField()
    image = models.ImageField(upload_to='blog',blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    # this class contains metadata and uses the created_on field from the model to sort out data which sorts
    # in descending order by default
    class Meta:
        ordering = ['-created_on']

    # this method is the default human-readable representation of the object. Django will use it in many places
    # such as the admin panel
    def __str__(self):
        return str(self.title)
    #
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)
