from django.http import HttpResponse
from django.template import Context,Template
from django.shortcuts import render_to_response

def index(request):
#    t = Template('<html><body><p>Template <p> client ip: {{ ip }}</body></html>')

    return render_to_response('index.html',{'ip': request.META['REMOTE_ADDR']})
