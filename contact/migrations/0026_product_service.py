# Generated by Django 5.0.1 on 2024-03-10 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0025_service_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_service', to='contact.service'),
        ),
    ]
