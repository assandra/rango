
from django.db import models
from django.template.defaultfilters import slugify

# Class for the model representing category
# which inherit the Model base class
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)



    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

# Class for the model representing page
# which inherit the Model base class
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)



    def __str__(self):
        return self.title