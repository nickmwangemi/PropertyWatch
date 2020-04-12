from django.db import models
from datetime import datetime

# Create your models here.
class Agent(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%d/%m/%Y/',blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tbl_Agents'