# Generated by Django 3.1.1 on 2021-02-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201005_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]