from django.template.loader import get_template
from django.shortcuts import render
from django.template import Context
from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    return render (request, 'current_datetime.html',{'current_date': now} )

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render (request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def display_meta(request):
    values = request.META.items()
    values = sorted(values)
    html = []
    for k,v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))