from django.db import models
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    name = models.CharField(max_length=128, unique = True)
    gender = models.CharField(max_length=128, unique = True)
    location = models.CharField(max_length=128, unique = True)
    state = models.CharField(max_length=128, unique = True)
    allergy = models.CharField(max_length=128, unique = True)
    health = models.CharField(max_length=128, unique = True)
    
    

    
    def __unicode__(self):
        return self.name