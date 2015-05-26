from django.http import HttpResponse, Http404
import datetime
from django.shortcuts import render_to_response



def hello(request):
    return HttpResponse("Hello World")

def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('current_date.html')
    # t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    # html = t.render(Context({'current_date': now}))
    return render_to_response('current_date.html', {'current_date': now})

def hour_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    #assert False
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
