from os import truncate
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils import timezone
import math
from django.db.models import Max

# Create your models here.
class user(models.Model):
    email=models.EmailField(unique=True,max_length=50)
    password=models.CharField(max_length=20)
    role=models.CharField(max_length=20)
    otp=models.IntegerField(default=450)
    is_active=models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
 

    def __str__(self):
        return self.email
class company(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=30)
    company_address=models.CharField(max_length=100)
    company_contact=models.IntegerField(max_length=30)
    company_city=models.CharField(max_length=20)
    company_type=models.CharField(max_length=20)
    company_established=models.CharField(max_length=100,default="")
    company_info=models.TextField(null=True,blank=True)
    company_emp=models.IntegerField(default=0)
    company_logo=models.FileField(upload_to='media/images/',default='media/default.png')
    company_cover=models.FileField(upload_to='media/images/',default='media/bgcover.png')

    def __str__(self):
        return self.company_name

class customer(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=30)
    customer_contact=models.IntegerField(max_length=30)
    customer_qualification=models.CharField(max_length=50)
    customer_address=models.CharField(max_length=100)
    
    def __str__(self):
        return self.customer_name 

    customer_logo=models.FileField(upload_to='media/images/',default='media/default.png')
    customer_cover=models.FileField(upload_to='media/images/',default='media/bgcover.png')

class company_gallary(models.Model):
    company_id=models.ForeignKey(company,on_delete=models.CASCADE)
    picture=models.FileField(upload_to='media/images',blank=True,null=True)

    def __str__(self):
        return self.company_id.company_name

class customer_gallary(models.Model):
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    picture=models.FileField(upload_to='media/images',blank=True,null=True)

    def __str__(self):
        return self.customer_id.customer_name

class jobpost(models.Model):
    company_id=models.ForeignKey(company,on_delete=models.CASCADE)
    job_title=models.CharField(max_length=50)
    job_description=models.TextField()
    job_type=models.CharField(max_length=30)
    job_salary=models.IntegerField()
    emp_requirement=models.IntegerField()
    job_tags=models.CharField(max_length=50)
    status=models.CharField(max_length=20,default="open")
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.job_title +"  added by  "+self.company_id.company_name
    def whenpublished(self):
        now=timezone.now()
        diff=now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds <60:
            seconds=diff.seconds
            if seconds==1:
                return str(seconds) + "seconds ago"
            else:
                 return str(seconds) + "seconds ago"
        if diff.days == 0 and diff.seconds >= 60 and diff.seconds <3600:
            minutes=math.floor(diff.seconds/60)
            if minutes==1:
                return str(minutes) + " minutes ago"
            else:
                 return str(minutes) + " minutes ago"

        if diff.days == 0 and diff.seconds >=3600  and diff.seconds <86400:
            hours=math.floor(diff.seconds/3600)
            if hours==1:
                return str(hours) + "hours ago"
            else:
                 return str(hours) + "hours ago"

        if diff.days >= 1 and diff.days<30:

            days=diff.days
            if days==1:
                return str(days) + "days ago"
            else:
                 return str(days) + "days ago"

        
        if diff.days >= 30 and diff.days<365:

            months=math.floor(diff.days/30)
            if months==1:
                return str(months) + "months ago"
            else:
                 return str(months) + "monthss ago"

        if diff.days >= 365:

            years=math.floor(diff.days/365)
            if years==1:
                return str(years) + "years ago"
            else:
                 return str(years) + "years ago"

    def mylikes(self):
        try:
            my_post_likes=postlike.objects.filter(jobpost_id=self.id).order_by('-likes')
            
            total_likes=my_post_likes[0].likes
            return total_likes
        except:
            return 0

    def mytags(self):
        my_alltags=self.job_tags.split(" , ")
        print("all my tags",my_alltags)
        return my_alltags
        
class postlike(models.Model):
    jobpost_id=models.ForeignKey(jobpost,on_delete=models.CASCADE)
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    likes=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)

    def __str__(self):
        return self.jobpost_id.job_title+"liked by"+self.customer_id.customer_name

class companyfollowers(models.Model):
    customer_id=models.ForeignKey(customer,on_delete=models.CASCADE)
    company_id=models.ForeignKey(company,on_delete=models.CASCADE)
    following_status=models.CharField(max_length=20,default="pending")
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)

 
    def __str__(self):
        return self.customer_id.customer_name+"following"+self.company_id.company_name
