from cgitb import handler
from enum import unique
from pickle import TRUE
from django.db import models
from django.urls import reverse

class Reporter(models.Model):
    full_name=models.CharField(max_length=70)

    def __str__(self):
        return self.full_name



class Article(models.Model):
    pub_date=models.DateField()
    headline=models.CharField(max_length=200)
    content=models.TextField()
    reporter=models.ForeignKey(Reporter,on_delete=models.CASCADE)
    
    #This is used to determine the property chosen to describe the class
    def __str__(self):
        return self.headline

# Create your models here.

GENDER_CHOICES=[
    ('F','F'),
    ('M',"M")
]
class The_member(models.Model):
    year_of_study=models.IntegerField()
    gender=models.CharField(max_length=6,choices=GENDER_CHOICES)
    leader_status =models.BooleanField(default=False)
    #leader_pre_status =models.BooleanField(default=False,null=True)

  #  def __str__(self):
  #      return str(self)

    def get_absolute_url(self):
      return reverse("Cool:member-detail",kwargs={"":self.id})  


#BibleStudy Members
class BStudyMember(models.Model):
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50)
    sir_name=models.CharField(max_length=50)
    level=models.IntegerField()
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    leader_status =models.BooleanField(default=False)
    phone_number=models.CharField(max_length=10,unique = True)



    def get_absolute_url(self):
        return reverse("Cool:member-detail",kwargs={"id":self.id})  
    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.sir_name}"


class Groups_BackUp(models.Model):
    name = models.CharField(max_length=10)
    info = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.name)


