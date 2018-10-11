"""
Definition of urls for RFIDWeb.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
import django.contrib.auth.views
from django.views.generic.base import RedirectView

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^live', app.views.live, name='live'),
    url(r'^archive/$', app.views.archive, name='archive'),
    url(r'^archive/dl/$', app.views.archive_dl, name='archive_dl'),
    url(r'^log/$', app.views.log, name='log'),
    url(r'^log/dl/$', app.views.log_dl, name='log_dl'),
    url(r'^watch/', app.views.watch, name='watch'),
    url(r'^watch2/', app.views.watch2, name='watch2'),
    url(r'^users', app.views.users, name='users'),
    url(r'^scanners', app.views.scanners_view, name='scanners'),
    url('pingscanners/$', app.views.pingscanners, name='pingscanners'),
    url(r'^data', app.views.data, name='data'),
    url(r'^clear/$', app.views.clear, name='clear'),
    url('clear_empty/$', app.views.clear_empty, name='clear_empty'),
    url('clear_unknown/$', app.views.clear_unknown, name='clear_unknown'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', favicon_view),
]
if settings.DEBUG:
  # static files (images, css, javascript, etc.)
  urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)