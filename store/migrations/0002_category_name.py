# Generated by Django 4.0.1 on 2022-02-27 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
    ]