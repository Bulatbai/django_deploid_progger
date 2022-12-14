# Generated by Django 4.0.6 on 2022-07-28 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('location', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('create_update', models.DateTimeField(auto_now=True)),
                ('amount_p', models.IntegerField(default=0)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('img', models.ImageField(blank=True, null=True, upload_to='places_img')),
                ('price', models.DecimalField(decimal_places=2, default=True, max_digits=50)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'место',
                'verbose_name_plural': 'Места',
                'ordering': ['name'],
            },
        ),
    ]
