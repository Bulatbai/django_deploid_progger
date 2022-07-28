from django.db import models

from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL,
                null=True, blank=True
                )
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    create_update = models.DateTimeField(auto_now=True)
    amount_p = models.IntegerField(default=0)
    photo = models.ImageField(null=True, blank=True)
    img = models.ImageField(upload_to='places_img',null=True, blank=True)
    price = models.DecimalField(max_digits=50,  decimal_places=2, default=True)





    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'Места'
        ordering = ['name']





class Comments(models.Model):
       post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='post_comment')
       text = models.TextField(verbose_name='coments')
       created_date = models.DateTimeField(auto_now_add=True)
        
