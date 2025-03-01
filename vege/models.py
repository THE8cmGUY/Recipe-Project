from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_des = models.TextField(null = False , blank = False)
    receipe_image = models.ImageField(upload_to="receipe")
    def __str__(self):
        return f'{self.receipe_name} - {self.receipe_des[:50]}'
    
   
    

