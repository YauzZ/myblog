from django.http import HttpResponse


def index(request):
    return HttpResponse('<html><body>clent ip: %s </body></html>' % request.META['REMOTE_ADDR'])
    pass
