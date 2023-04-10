from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#code passward
class UserModel(AbstractUser):
    class Meta:
        db_table = "my_user"
    email = models.EmailField(max_length=50, unique=True)

class SignUpModel(UserModel):
    password_check1 = models.CharField(max_length=20)
    password_check2 = models.CharField(max_length=20)