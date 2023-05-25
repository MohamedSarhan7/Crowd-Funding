# Generated by Django 4.2.1 on 2023-05-24 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_alter_project_avgrage_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='project',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='project',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='project',
        ),
        migrations.RemoveField(
            model_name='rate',
            name='user',
        ),
        migrations.RemoveField(
            model_name='report',
            name='project',
        ),
        migrations.RemoveField(
            model_name='report',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='api.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='project',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='api.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rate',
            name='project',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='api.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rate',
            name='user',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='project',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='api.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
