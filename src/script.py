>>> import json
whith open("/f/devlabs/py/cvt/src/skills.json", "r") as f:
data = json.load(f)

for s in data:
    Skills.objects.create(category=s["category"], skill=s{"skills"], level_skill=s["level_skill"])
