# Generated by Django 4.0 on 2021-12-21 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/project_image'),
        ),
    ]
