# Generated by Django 4.0 on 2022-01-04 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]