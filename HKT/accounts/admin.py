from django.contrib import admin
from .models import Profile

# Register your models here.
class YourModelAdmin(admin.ModelAdmin):

    list_display = ('user','UID')

admin.site.register(Profile, YourModelAdmin)