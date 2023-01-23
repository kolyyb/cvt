from django.urls import path
from .views import json
from .views import index
from .views import skills
from .views import mission


urlpatterns = [
    path('', index, name="curvi-index"),
    path('json/', json, name="json"),
    path('mission/', mission, name="mission"),
    path('skills/', skills, name="skills"),

]