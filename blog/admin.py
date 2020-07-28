from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.

#A connection of the Post Model to the admin pannel.
admin.site.register(Post)

#A connection of the Comment Model to the admin pannel.
admin.site.register(Comment)
