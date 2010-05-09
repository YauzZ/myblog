from django.http import HttpResponse
from django.template import Context,Template

def index(request):
    t = Template('<html><body><p>Template <p> client ip: {{ ip }}</body></html>')
    c = Context({'ip': request.META['REMOTE_ADDR']})
    html = t.render(c)
    return HttpResponse(html)
