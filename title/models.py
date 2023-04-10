from django.db import models
from user.models import UserModel

# Create your models here.
class TitleModel(models.Model):
    class Meta:
        db_table="title"

    writer=models.ForeignKey(UserModel, on_delete=models.SET_DEFAULT, default=1)
    title=models.CharField(max_length=256)
    content=models.CharField(max_length=256)
    image=models.FileField(upload_to=None,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.title
