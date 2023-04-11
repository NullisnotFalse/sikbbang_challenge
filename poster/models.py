from django.db import models
from user.models import UserModel

# Create your models here.
class PosterModel(models.Model):
    class Meta:
        db_table="poster"

    writer=models.ForeignKey(UserModel, on_delete=models.SET_DEFAULT, default=3)#default값은 my_user id값 확인필요
    title=models.CharField(max_length=256)
    content=models.CharField(max_length=256)
    image=models.FileField(upload_to='imgs/poster/',null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.title
