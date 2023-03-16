# Generated by Django 4.1.7 on 2023-03-09 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_product_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='year',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='myapp.year'),
            preserve_default=False,
        ),
    ]
