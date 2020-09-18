from django.db import models

# Create your models here.


class Accounts(models.Model):
    image = models.ImageField(upload_to='media/')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    unique_id = models.CharField(max_length=20)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name

        

