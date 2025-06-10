from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='banner_images/')

    def __str__(self):
        return self.title
    
    