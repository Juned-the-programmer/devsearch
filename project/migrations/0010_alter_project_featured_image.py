# Generated by Django 4.0 on 2022-01-09 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='static/project_image'),
        ),
    ]
