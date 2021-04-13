from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Workouts(models.Model): 
    user_id = models.IntegerField()
    date = models.DateTimeField()
    length = models.DecimalField(max_digits=4, decimal_places=1)
    type = models.CharField(max_length=200)
    calories = models.IntegerField()
    goal_id = models.IntegerField()

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField() 
    gender = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    height = models.DecimalField(max_digits=3, decimal_places=1)

class Goals(models.Model): 
    name = models.CharField(max_length=200) 
    points = models.IntegerField()

class Videos(models.Model):
    # this isn't really all that special, just allows us to easily add videos from admin page instead of having to update the HTML and repush
    # this is the embed stuff you get from the YouTube share option 
    embed = models.CharField(max_length=300)
    # this holds a short description about the content of each video
    description = models.CharField(max_length=200)

class ForumPost(models.Model):
    """
    The forumPost object will be associated with a particular user, have a 
    """