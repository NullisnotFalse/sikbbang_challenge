from django.db import models

class CommentModel(models.Model):
    class Meta:
        db_table="comment"
    content=models.CharField(max_length=256)
    image=models.FileField(upload_to=None,null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
