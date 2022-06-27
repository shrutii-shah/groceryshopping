# Generated by Django 4.0.5 on 2022-06-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=400)),
                ('address_info', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
