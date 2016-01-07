from .models import Post, Comment  	# import Comment as well
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)  		#register our model
