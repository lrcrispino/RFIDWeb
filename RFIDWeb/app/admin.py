
from django.contrib import admin
from .models import rawdata
from .models import accesslog
from .models import userlist
from .models import scanners

admin.site.register(rawdata)
admin.site.register(accesslog)
admin.site.register(userlist)
admin.site.register(scanners)