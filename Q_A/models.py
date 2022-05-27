from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils.text import slugify
from numpy import character
# Create your models here.
class questions(models.Model): #creating question table
    question = models.CharField(max_length=150)
    def __str__(self): 
        return '%s. %s'%(self.id,self.question)

class characters(models.Model): #creating question table
    character = models.CharField(max_length=50)
    def __str__(self): 
        return '%s. %s'%(self.id,self.character)

class answers(models.Model): #creating question table
    answer = models.CharField(max_length=150)
    Q_ID = models.ForeignKey('questions',on_delete=CASCADE)
    Char_ID = models.ForeignKey('characters',on_delete=CASCADE)
    Char = models.CharField(max_length=1)
    def __str__(self): 
        return self.Char
