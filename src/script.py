from curvi.models import Missions
import json


def inject_datas():
    with open("./missions.json", "r") as f:
        data = json.load(f)

    for s in data:
        Missions.objects.create(client=s["client"], role=s["role"], date_in=s["date_in"], date_out=s["date_out"], project=s["project"], description=s["description"], stack=s["stack"])


inject_datas()

# IMPORT DATAFILE IN PYTHON SHELL : exec(open('python_file.py').read())
