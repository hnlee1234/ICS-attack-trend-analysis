# Generated by Django 2.0.6 on 2018-09-03 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20180903_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='treeitem',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='TreeItem',
        ),
    ]