from django.db import models
from django.contrib.auth.models import User

from datetime import date

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateofbirth = models.DateField()

    @property
    def age(self):
        today = date.today()
        return today.year - self.dateofbirth.year - ((today.month, today.day) < (self.dateofbirth.month, self.dateofbirth.day))
