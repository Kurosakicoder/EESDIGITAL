# Generated by Django 3.0.2 on 2020-01-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('important_notice', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Home',
            },
        ),
    ]
