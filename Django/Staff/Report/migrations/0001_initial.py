# Generated by Django 3.2.6 on 2021-11-30 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=100)),
                ('staff_name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('salary', models.CharField(max_length=100)),
            ],
        ),
    ]
