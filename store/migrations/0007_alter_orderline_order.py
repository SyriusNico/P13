# Generated by Django 4.0.1 on 2022-04-03 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_order_address1_alter_order_address2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.order'),
        ),
    ]
