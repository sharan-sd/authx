from django.db import models

# User Accounts Model
class UserAccounts(models.Model):
    email = models.EmailField(max_length=75, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
