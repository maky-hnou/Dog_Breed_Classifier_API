from django.contrib import admin

from .models import ImageModel


class ImageModelAdmin(admin.ModelAdmin):
    search_fields = [field.name for field in ImageModel._meta.get_fields()]
    list_display = [field.name for field in ImageModel._meta.get_fields()]
    list_filter = ('processed', 'upload_date', 'category',)


admin.site.register(ImageModel, ImageModelAdmin)
