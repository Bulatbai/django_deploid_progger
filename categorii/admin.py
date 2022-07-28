from django.contrib import admin
from .models import Post,   Comments

admin.site.register(Post)



admin.site.register(Comments)


# class Feedbackadmin(admin.ModelAdmin):
#     list_display = ['text','place', 'user', 'checked']
#     list_editable = ['checked']
#     list_filter = ['checked']
#     search_fields = ['text','place__name','place__location']
    
#     fields = ['text','user', 'checked']

#     # readonly_fields = ['text','place']

# admin.site.register(Feedback, Feedbackadmin)
