from django.db import models

# Create your models here.
class Song(models.Model):
    name=models.CharField(max_length=250)
    feat=models.TextField()
    image=models.ImageField(upload_to='song')
    
    
    def _str_(self):
        return self.song

