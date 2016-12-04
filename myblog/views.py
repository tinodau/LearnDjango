# from django.template.loader import get_template
# from django.template import Context
# from django.http import HttpResponse

from django.shortcuts import render

import datetime

# Create your views here.
def hello(request):
    return HttpResponse('hello world')


def current_time(request):
    now = datetime.datetime.now()

    return render(request, 'current_datetime.html', {'current_date': now})

    # html = "<html><body>It's now %s</body></html>" % now

    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date' : now}))
    # return HttpResponse(html)
