# Generated by Django 2.1.7 on 2019-03-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videorequest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videotitle',
            field=models.CharField(max_length=30),
        ),
    ]