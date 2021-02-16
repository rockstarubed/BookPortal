# Generated by Django 2.2.11 on 2021-02-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'FeedBack',
            },
        ),
    ]