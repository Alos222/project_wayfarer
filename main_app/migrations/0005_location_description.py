# Generated by Django 4.0.2 on 2022-02-15 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.CharField(default='', max_length=250),
        ),
    ]