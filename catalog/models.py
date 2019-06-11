from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50,unique=True,blank=False)
    organisation = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=32, default='pass4user', blank=False)

    def __str__(self):
        return self.username

class Admin(models.Model):
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length=20, default='DBAdmin', editable=False)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admins')

    def __str__(self):
        return self.username




