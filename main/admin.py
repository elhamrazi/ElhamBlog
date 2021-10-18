from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Comment)

# Register your models here.
