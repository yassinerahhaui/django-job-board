from django.db import models
from djmoney.models.fields import MoneyField
import uuid
from django.contrib.auth.models import User

# Create your models here.
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

#########################################################################

def image_upload(instance,filename):
    imagename, extansion = filename.split('.')
    return f'jobs/{uuid.uuid4()}.{extansion}'

            ##############################

class Job(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20,choices=JOB_TYPE)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.IntegerField(default=1)
    salary = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(allow_unicode=True,blank=True,null=True,max_length=100)

    def __str__(self):
        return self.title
    
    ###############################

    def save(self,*args,**kwargs):
        self.slug = self.title.replace(" ", "-")
        super(Job,self).save(*args,**kwargs)

##########################################################################

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

###########################################################################

class Apply(models.Model):
    job = models.ForeignKey('JOB', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=200)
    cv = models.FileField(upload_to='cv/')
    cover_letter = models.TextField(max_length=1000)

    def __str__(self):
        return self.name