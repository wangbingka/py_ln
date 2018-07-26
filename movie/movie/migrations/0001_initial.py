# Generated by Django 2.0.7 on 2018-07-25 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('movie_name', models.CharField(max_length=255)),
                ('img_url', models.URLField()),
                ('rate', models.IntegerField()),
            ],
        ),
    ]
