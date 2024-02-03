from django.contrib import admin

# Register your models here.
from .models import uploadfile


class YourModelAdmin(admin.ModelAdmin):
    list_display = ["file_upload"]  # Add any other fields you want to display

admin.site.register(uploadfile, YourModelAdmin)
