from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#code passward
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
    email = models.EmailField(max_length=50, unique=True)
