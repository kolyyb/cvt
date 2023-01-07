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
    LEVEL_SKILLS = (
        ('F', 'Fondamentaux'),
        ('N', 'Novice'),
        ('I', 'Intermediaire'),
        ('E', 'Expert'),
    )
    category = models.CharField(max_length=100)
    skills = models.TextField()
    level_skill = models.CharField(max_length=1, choices=LEVEL_SKILLS)

class Training(models.Model):
    name = models.CharField(max_length=100)
    graduate = models.CharField(max_length=100)
    training_center = models.CharField(max_length=100)
    graduate_date = models.DateField(null=False)

class Missions(models.Model):
    client = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date_in = models.DateField(null=False)
    date_out = models.DateField(null=False)
    role = models.CharField(max_length=100)
    project = models.CharField(max_length=250)
    stack = models.TextField()





