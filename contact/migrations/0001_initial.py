# Generated by Django 3.1.4 on 2021-02-02 13:44

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
                ('full_name', models.CharField(max_length=50)),
                ('relationship', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
