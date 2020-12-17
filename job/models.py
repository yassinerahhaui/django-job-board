from django.db import models
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20,choices=JOB_TYPE)
    description = models.TextField()
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    phone_number = PhoneNumberField()
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title