# Generated by Django 5.0.6 on 2024-06-30 23:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_description_alter_product_promotions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='feature_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='store.product'),
        ),
    ]