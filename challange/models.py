from django.db import models

class ChallangeModel(models.Model):
    class Meta:
        db_table="Challange"
    content=models.CharField(max_length=256)
    image=models.FileField(upload_to="imgs/challange/",null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)