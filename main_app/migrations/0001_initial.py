from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=100)),
                ('img', pyuploadcare.dj.models.ImageField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WayfarerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('img', pyuploadcare.dj.models.ImageField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=2000)),
                ('content_img', pyuploadcare.dj.models.ImageField(blank=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main_app.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='main_app.wayfareruser')),
            ],
        ),
    ]
