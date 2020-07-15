from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post) # To make model visible in the admin page