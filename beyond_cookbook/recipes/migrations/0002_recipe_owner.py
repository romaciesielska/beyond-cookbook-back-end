# Generated by Django 2.2 on 2020-02-10 22:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]
