from django.db import models

# Create your models here.


class Accounts(models.Model):
    user_name = models.CharField(max_length=20, null=True)
    college_name = models.CharField(max_length=100, null=True)
    degree = models.CharField(max_length=100, null=True)
    passout_year = models.PositiveIntegerField(null=True)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    school_name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(null=True)
    course = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.email_id

        






