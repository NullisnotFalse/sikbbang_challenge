# Generated by Django 4.2 on 2023-04-11 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='image',
            field=models.FileField(null=True, upload_to='imgs/comment/'),
        ),
    ]