# Generated by Django 4.0.1 on 2022-03-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='postcode',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
