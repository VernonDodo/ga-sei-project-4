from django.db import models

class User(models.Model):
    email = models.EmailField(max_length=50,unique=True,blank=False)
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=32, default='pass4user', blank=False)

    def __str__(self):
        return self.email

class Admin(models.Model):
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admins')
    role = models.CharField(max_length=20, default='DBAdmin', editable=False)
    
    def __str__(self):
        return self.firstname

class Producer(models.Model):
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='producers')
    organisation = models.CharField(max_length=100, blank=False)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.organisation





