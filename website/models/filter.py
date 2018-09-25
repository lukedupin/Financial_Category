from django.db import models
from django.contrib import admin

from website.models.category import Category

  #Defines an object whos duty is to hold pay rate information
class Filter(models.Model):
    # define my models
    id              = models.AutoField(primary_key=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)

    name            = models.CharField(max_length=64)
    regex           = models.CharField(max_length=64)

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
        class FilterAdmin(admin.ModelAdmin):
            pass

        return ( FilterAdmin, None )[idx]

