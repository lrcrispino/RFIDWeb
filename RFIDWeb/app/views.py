"""
Definition of views.
"""
import csv
import time
from django.utils import timezone
from django.utils.encoding import smart_str
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from .models import rawdata
from .models import accesslog
from .models import userlist
from .models import scanners
import mqtt

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home',
            'year':datetime.now().year,
        }
    )

def live(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/live.html',
        {
            'title':'Live View',
            'year':datetime.now().year,
        }
    )

def archive(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    log_list = accesslog.objects.all()
    return render(
        request,
        'app/archive.html',
        {
            'title':'Log Archive',
            'year':datetime.now().year,
            'log_list':log_list,
        }
    )

def log(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    log_list = accesslog.objects.filter(entrydate__date=timezone.datetime.today())
    return render(
        request,
        'app/log.html',
        {
            'title':'Daily Activity Log',
            'year':datetime.now().year,
            'log_list':log_list,
        }
    )
def users(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    user_list = userlist.objects.all()
    return render(
        request,
        'app/users.html',
        {
            'title':'Users',
            'year':datetime.now().year,
            'user_list':user_list,
        }
    )

def scanners_view(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    scanner_list = scanners.objects.all()
    return render(
        request,
        'app/scanners.html',
        {
            'title':'Scanners',
            'year':datetime.now().year,
            'scanner_list':scanner_list,
        }
    )

def watch(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    watch_list = userlist.objects.filter(status="in", area=request.GET.get('stn'))
    return render(
        request,
        'app/watch.html',
        {
            'title':request.GET.get('stn')+' Status',
            'year':datetime.now().year,
            'action':accesslog.objects.last().action,
            'watch_list':watch_list,
        }
    )

def watch2(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    watch_list = userlist.objects.filter(status="in")
    return render(
        request,
        'app/watch2.html',
        {
            'title':'Live Watch2',
            'year':datetime.now().year,
            'watch_list':watch_list,
        }
    )

def data(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    datas = rawdata.objects.get(pk=1)
    return render(
        request,
        'app/data.html',
        {
            'title':'Raw Data',
            'message':'Data recieved from MQTT server',
            #'data':rawdata,
            'datas':datas.text,
            'year':datetime.now().year,
        }
    )

def clear(request):
    datas1 = rawdata.objects.get(pk=1)
    datas1.text = ""
    datas1.save()
    return HttpResponseRedirect('/data')

def archive_dl(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RFID Archive '+str(timezone.localtime())[0:18]+'.csv"'
 
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"Date"),
        smart_str(u"Area"),
        smart_str(u"ID"),
        smart_str(u"Username"),
        smart_str(u"Scan"),
        smart_str(u"Action"),
    ])
    log_list = accesslog.objects.all()
    for log in log_list:
        writer.writerow([
            smart_str(str(log.entrydate)[0:18]),#trim microseconds
            smart_str(log.area),
            smart_str(log.scan_id),
            smart_str(log.username),
            smart_str(log.scan_type),
            smart_str(log.action),
        ])
    return response

def log_dl(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="RFID Daily log '+str(timezone.localtime())[0:18]+'.csv"'
 
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow([
        smart_str(u"Date"),
        smart_str(u"Area"),
        smart_str(u"ID"),
        smart_str(u"Username"),
        smart_str(u"Scan"),
        smart_str(u"Action"),
    ])
    log_list = accesslog.objects.filter(entrydate__date=timezone.datetime.today())
    for log in log_list:
        writer.writerow([
            smart_str(str(log.entrydate)[0:18]),#trim microseconds
            smart_str(log.area),
            smart_str(log.scan_id),
            smart_str(log.username),
            smart_str(log.scan_type),
            smart_str(log.action),
        ])
    return response

def clear_empty(request):
    found = accesslog.objects.filter(username="default")
    found.delete()
    return HttpResponseRedirect('/archive')

def clear_unknown(request):
    found = accesslog.objects.filter(username=userlist.objects.get(scan_id = "0"))
    found.delete()
    return HttpResponseRedirect('/archive')

def pingscanners(request):
    allscanners = scanners.objects.all()
    allscanners.update(online=False)
    mqtt.pingscanners()
    time.sleep(1)
    return HttpResponseRedirect('/scanners')