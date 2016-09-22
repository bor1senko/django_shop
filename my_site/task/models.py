from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title.encode('utf-8')


class Product(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100 )
    image = models.ImageField(null=True, blank=True)
    price = models.FloatField()
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return unicode(self.title)

class PropertyGroup(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title.encode('utf8')

    def __unicode__(self):
        return self.title

class PropertyName(models.Model):
    bool = 'bool'
    str = 'str'
    type_choices = (
        (bool, 'boolean'),
        (str, 'string'),
    )
    name = models.CharField(max_length=150)
    type =models.CharField(max_length=100, choices=type_choices)
    product = models.ForeignKey(PropertyGroup)

    def __str__(self):
        return self.name.encode('utf-8')

    def __unicode__(self):
        return self.name

class BooleanProperty(models.Model):
    key =  models.ForeignKey(PropertyName)
    value = models.BooleanField(blank=True)
    product = models.ForeignKey(Product)
    group = models.ForeignKey(PropertyGroup)

    def __str__(self):
        return str(self.key)

    def __unicode__(self):
        return unicode(self.key)

class StringProperty(models.Model):
    key = models.ForeignKey(PropertyName)
    value = models.CharField(max_length=100, blank=True)
    product = models.ForeignKey(Product)
    group = models.ForeignKey(PropertyGroup)

    def __str__(self):
        return str(self.key)

    def __unicode__(self):
        return unicode(self.key)

class Comment(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product)
    data = models.DateTimeField(auto_now=True)

@receiver(post_save, sender=Product)
def add_property(instance, **kw):
    AllPropertyGroup = PropertyGroup.objects.filter(category__exact=instance.category)
    all_bool_property = [item.key for item in BooleanProperty.objects.filter(product__exact=instance)]
    all_str_property = [item.key for item in StringProperty.objects.filter(product__exact=instance)]
    for item in AllPropertyGroup:
        for e in  PropertyName.objects.filter(product__exact=item):
            if e.type == 'bool':
                if e not in all_bool_property:
                    obj = BooleanProperty(key=e, value='', product=instance, group=item)
                    obj.save()
            elif e.type == 'str':
                if e not in all_str_property:
                    obj = StringProperty(key=e, value='', product=instance, group=item)
                    obj.save()
