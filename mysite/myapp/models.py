from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
User = settings.AUTH_USER_MODEL
class Cource(models.Model):
    course_name = models.CharField(max_length=100)

class Enquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    Full_Name=models.CharField(max_length=250,default="")
    gender=models.CharField(max_length=10)
    Email_Address=models.EmailField()
    Contact_Number=models.IntegerField() 
    Permanent_Address=models.TextField(blank=True,null=True,default='')
    Date_of_Birth=models.DateField(auto_now_add=False,null=True,blank=True)   
    massage=models.TextField(blank=True,null=True)
    Whatsapp_Number=models.IntegerField(blank=True,null=True)
    Alternate_Number=models.IntegerField(blank=True,null=True)
    How_did_you_hear_about_us=models.CharField(null=True,max_length=50)
    qualification=models.CharField(max_length=50,null=True,blank=True)
    Technical_Skills=models.CharField(max_length=150,null=True,blank=True)
    Certification_Done=models.CharField(max_length=200,null=True,blank=True)
    Area_of_Intrest=models.CharField(max_length=200,null=True,blank=True)
    reference=models.CharField(max_length=100,null=True,blank=True)
    remark=models.CharField(max_length=100,null=True,blank=True)
    Training_Mode=models.CharField(max_length=50,blank=True,null=True)
    Office_Location_Preference=models.CharField(max_length=50,null=True,blank=True)
   
    STATUS = (
        ('Finalized', 'Finalized'),
        ('Pending', 'Pending'),
        ('Informed_On_whatsapp','Informed_On_whatsapp')
        
    )
    enquiry_Status = models.TextField(max_length=100, choices=STATUS, default="Pending",null=True)
    Cource_name=models.ForeignKey(Cource,on_delete=models.CASCADE,null=True,blank=True)

class User(AbstractUser):
    # email = models.EmailField(unique=True)
    is_admin= models.BooleanField('Is admin',default=False)
    is_enquiry = models.BooleanField('Is enquiry',default=False)
    is_account = models.BooleanField('Is account',default=False)
    is_it = models.BooleanField('Is it',default=False)
    is_hr = models.BooleanField('Is hr',default=False)
    is_training = models.BooleanField('Is training',default=False)

