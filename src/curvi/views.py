from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from curvi.models import Missions


def index(request):
    return HttpResponse('Accueil index de curvi')
def json(request):
    json_res = JsonResponse({"1": "changement de status code avec JsonResponse !"})
    json_res.status_code = 403
    return json_res

def mission(request):
    try:
        Mission = Missions.objects.get(pk=2)
    except Missions.DoesNotExist:
        raise Http404("Cette mission ID 1 n'existe pas...")

    return HttpResponse(Mission.description)

def skills(request):
    return render(request, "curvi/curvi.html")