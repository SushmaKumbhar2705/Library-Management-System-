from django.db import models
from datetime import datetime,timedelta
 

#Create your models here.

class Book(models.Model):
    student_name = models.CharField(max_length=150)
    enrollment = models.IntegerField()
    book_name = models.CharField(max_length=150)
    author_name = models.CharField(max_length=150)
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(null=True)
    fine = models.IntegerField(null=True)


    
    
    def __str__(self):
        return self.student_name


