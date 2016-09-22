from django.contrib import admin

from .models import Category, Product, PropertyGroup, BooleanProperty, StringProperty, PropertyName


def MyIsinstance(obj):
    if isinstance(obj, BoolProperrtyInline):
        return True
    elif isinstance(obj, StrPropertyInline):
        return True
    else:
        return False

class BoolProperrtyInline(admin.TabularInline):
    model = BooleanProperty
    extra = 0
    fields = ('key', 'value')

class StrPropertyInline(admin.TabularInline):
    model = StringProperty
    extra = 0
    fields = ('key', 'value')

class ProductAdmin(admin.ModelAdmin):
    inlines = [BoolProperrtyInline, StrPropertyInline]

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if MyIsinstance(inline) and obj is None:
                continue
            yield inline.get_formset(request, obj), inline

class PropertyNameInline(admin.TabularInline):
    model = PropertyName
    extra = 1

class PropertyGroupAdmin(admin.ModelAdmin):
    inlines = [PropertyNameInline]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(PropertyGroup, PropertyGroupAdmin)
