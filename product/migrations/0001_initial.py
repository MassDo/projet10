# Generated by Django 2.2.7 on 2019-11-29 14:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('image', models.URLField()),
                ('link', models.URLField()),
                ('nutriscore', models.CharField(max_length=50)),
                ('fat', models.FloatField()),
                ('salt', models.FloatField()),
                ('sugars', models.FloatField()),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['category', 'nutriscore', 'fat', 'sugars', 'salt'],
            },
        ),
    ]
