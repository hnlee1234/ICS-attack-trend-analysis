# Generated by Django 2.0.6 on 2018-07-02 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180627_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='vulner',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]