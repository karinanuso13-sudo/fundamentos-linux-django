from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from base.models import BasePublishModel
from .validators import validate_blocked_words

# Create your models here.
class ProductModel(BasePublishModel):

    name = models.TextField()
    price = models.FloatField()

    description = models.TextField(blank=True, null=True)
    seller = models.CharField(max_length=120, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    product_dimensions = models.CharField(max_length=120, blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, db_index=True)

    def get_absolute_url (self):
        return f"/product/{self.slug}"

    def save(self, *args, **kwargs):
        validate_blocked_words(self.name)
        super().save(*args, **kwargs)
    
def slugify_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None or instance.slug == "":
        new_slug = slugify(instance.name)
        MyClass = instance.__class__
        qs = MyClass.objects.filter(slug__startswith= new_slug).exclude(id=instance.id)
        if qs.count() == 0:
            instance.slug = new_slug
        else:
            instance.slug= f"{new_slug}-{qs.count()}"
pre_save.connect(slugify_pre_save, sender=ProductModel) 