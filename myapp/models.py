from django.db import models

class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)
    u_type = models.CharField(max_length=100)


class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.fname

