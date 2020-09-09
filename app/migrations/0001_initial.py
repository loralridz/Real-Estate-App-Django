# Generated by Django 3.0.8 on 2020-07-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=200)),
                ('sname', models.CharField(default='', max_length=200)),
                ('email', models.EmailField(default='', max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
