# Generated by Django 2.0.6 on 2018-09-03 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_test_treeitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.RemoveField(
            model_name='treeitem',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='treeitem',
            name='parent',
        ),
        migrations.AddField(
            model_name='company',
            name='iscompany',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='company',
            name='main_division',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='company',
            name='paper1',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='company',
            name='paper2',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='company',
            name='refer',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='company',
            name='relation_level',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='company',
            name='sub_division',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='TreeItem',
        ),
    ]
