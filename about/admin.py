from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest

# Register your models here.

@admin.register(About)
class PostAdmin(SummernoteModelAdmin):
    """
    Enables Admin to see content of posts(?).
    """

    summernote_fields = ('content',)

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Enables the admin to read a collaboration message
    and send a "read" info to the composer. 
    """

    list_display = ('message', 'read',)