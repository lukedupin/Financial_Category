from django.contrib import admin
from django.utils.translation import ugettext_lazy
from django.contrib.auth.models import Group, User

from website.models import Account, Category, Entry, Filter

class MyAdminSite( admin.AdminSite ):
      # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Finances')

    # Text to put in each page's <h1>.
    site_header = ugettext_lazy('Finances')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Finances admin')
admin_site = MyAdminSite()

  #System level tables
admin_site.register( User )
admin_site.register( Group )

  #Import my table modules
admin_site.register( Account, Account.customAdmin() )
admin_site.register( Category, Category.customAdmin() )
admin_site.register( Entry, Entry.customAdmin() )
admin_site.register( Filter, Filter.customAdmin() )
