from django.http import HttpResponse


def index(request):
    return HttpResponse('Accueil index de cvt')

