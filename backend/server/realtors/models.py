from django.db import models

class Realtor(models.Model):
    """a model to hold realtors info"""
    profile_picture = models.ImageField(upload_to='profile_pictures/%Y/%m/%d')
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    date_hired = models.DateTimeField(auto_now_add=True)
    top_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.name
