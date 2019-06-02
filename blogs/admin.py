from django.contrib import admin
from .models import BlogPost ,Categories, Author
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Categories)
admin.site.register(Author)