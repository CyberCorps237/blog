from django.contrib import admin
from django.utils.html import strip_tags
from blog_cybercorpscm.models import Message, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','titre','sous_titre','nom_poster','date_post')

admin.site.register(Post, PostAdmin)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','nom','telephone','email','contenu','date')