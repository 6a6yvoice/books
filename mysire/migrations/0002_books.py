# Generated by Django 4.2.3 on 2023-07-28 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titles', models.CharField(max_length=200)),
                ('categories', models.CharField(max_length=200)),
            ],
        ),
    ]
