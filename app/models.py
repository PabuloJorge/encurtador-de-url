from django.db import models


# Create your models here.
class sites(models.Model):
    codigo = models.CharField(max_length=150, primary_key=True, serialize=False)
    url = models.CharField(max_length=150)
