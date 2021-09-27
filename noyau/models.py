from django.db import models
from datetime import datetime

# Create your models here.
class Netfeelex(models.Model):
    Titre_filme = models.CharField(max_length=200)
    Contenu_filme = models.TextField()
    Date_publie = models.DateTimeField("Date publié",default =datetime.now())

def __str__(self): 
    return self.Titre_filme
