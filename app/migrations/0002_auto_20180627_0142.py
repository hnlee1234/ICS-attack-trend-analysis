# Generated by Django 2.0.6 on 2018-06-26 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=100, primary_key=True, serialize=False),
        ),
    ]
