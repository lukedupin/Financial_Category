from django.db import models
from django.contrib import admin

from website.models.account import Account
from website.models.category import Category
from website.models.filter import Filter

  #Defines an object whos duty is to hold pay rate information
class Entry(models.Model):
    #define my models
    id              = models.AutoField(primary_key=True)
    account         = models.ForeignKey(Account, on_delete=models.CASCADE)
    filter          = models.ForeignKey(Filter, on_delete=models.CASCADE)

    name            = models.CharField(max_length=64)
    amount          = models.DecimalField(max_digits=12,decimal_places=2)

    timestamp       = models.DateField()

    class Meta:
        app_label = 'website'

    #Returns a friendly name for the admin interface
    def __str__(self):
        return self.name

    @staticmethod
    def getById( id ):
        try:
            return Entry.objects.get(id=int(id))
        except Entry.DoesNotExist:
            return None

    @staticmethod
    def getOrNew( name, amount, timestamp ):
        try:
            entries = Entry.objects.filter(name=name, amount=amount, timestamp=timestamp)
            if len(entries) > 0:
                return entries[1]

            return Entry(name=name, amount=amount, timestamp=timestamp)

        except Entry.DoesNotExist:
            return None

    @staticmethod
    def customAdmin( idx=0 ):
        class EntryAdmin(admin.ModelAdmin):
            pass

        return ( EntryAdmin, None )[idx]

