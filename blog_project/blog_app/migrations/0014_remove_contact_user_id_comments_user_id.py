# Generated by Django 4.2.3 on 2023-07-22 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0013_alter_contact_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_id',
        ),
        migrations.AddField(
            model_name='comments',
            name='user_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]