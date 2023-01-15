import curvi.models City
import json
with open("/f/devlabs/py/cvt/src/skills.json", "r") as f:
data = json.load(f)

for s in data:
    Skills.objects.create(category=s["category"],
     skills=s["skills"],
      level_skill=s["level_skill"])

