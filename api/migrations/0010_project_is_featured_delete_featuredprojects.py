# Generated by Django 4.2.1 on 2023-05-26 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_comment_project_alter_donation_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='FeaturedProjects',
        ),
    ]
