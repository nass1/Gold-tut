from __future__ import unicode_literals

from django.db import models

class Treasure(models.Model):
    name = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)
    def __str__(self):
        return self.name

#"(name='Fools Gold', value=200, material= 'Rock',location='Sydney',img_url="link2")"