from django.contrib import admin
from .models import Post,   Comments

admin.site.register(Post)



admin.site.register(Comments)


# class Feedbackadmin(admin.ModelAdmin):
#     list_display = ['text','place', 'user','id']
#     list_editable = ['id']
#     list_filter = ['id']
#     search_fields = ['text','place__name','place__location']
    
#     fields = ['text','user', 'id']

#     # readonly_fields = ['text','place']

# admin.site.register(Post, Feedbackadmin)
