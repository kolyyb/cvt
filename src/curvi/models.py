from django.db import models


class Infos(models.Model):
    name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(null=False)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    links = models.URLField()


class Profile(models.Model):
    intro = models.TextField(null=False)


class Skills(models.Model):
    mission_skill = models.ManyToManyField("Missions")
    LEVEL_SKILLS = (
        ('F', 'Fondamentaux'),
        ('N', 'Novice'),
        ('I', 'Intermediaire'),
        ('E', 'Expert'),
    )
    category = models.CharField(max_length=100)
    skills = models.TextField()
    level_skill = models.CharField(max_length=1, choices=LEVEL_SKILLS)

    @property
    def levelskill_string(self):
        if self.level_skill == "N":
            return "Plutôt débutant sur cette compétence"
        elif self.level_skill == "I":
            return "Plutôt un bon niveau de compétence"
        elif self.level_skill == "E":
            return "Plutôt une bonne expertise sur cette compétence"
        return "0 compétence"


class Training(models.Model):
    name = models.CharField(max_length=100)
    graduate = models.CharField(max_length=100)
    training_center = models.CharField(max_length=100)
    graduate_date = models.DateField(null=False)


class Missions(models.Model):
    city_mission = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    client = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    date_in = models.DateField(null=False)
    date_out = models.DateField(null=False)
    project = models.CharField(max_length=250)
    description = models.TextField(default="")
    stack = models.TextField()


class Location(models.Model):
    city = models.CharField(max_length=50)
