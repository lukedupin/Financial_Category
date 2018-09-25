from django.db import models
from django.contrib import admin

  #Defines an object whos duty is to hold pay rate information
class Category(models.Model):
    id              = models.AutoField(primary_key=True)

    name            = models.CharField(max_length=64)

    updated_on      = models.DateTimeField(auto_now=True)
    created_on      = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'website'

    #Returns a friendly name for the admin interface
    def __str__(self):
        return self.name

    @staticmethod
    def getById( id ):
        try:
            return Radius.objects.get(id=util.xint(id))
        except Radius.DoesNotExist:
            return None

    @staticmethod
    def customAdmin( idx=0 ):
        class CategoryAdmin(admin.ModelAdmin):
            pass

        return ( CategoryAdmin, None )[idx]

