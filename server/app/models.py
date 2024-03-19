from django.db import models

# Create your models here.
class TestModel(models.Model):
    string = models.CharField(max_length=100)
    number = models.IntegerField()
    check = models.BooleanField()

    def save(self, *args, **kwargs):
        if self.number < 10:
            return
        super().save(*args, **kwargs)