# Generated by Django 5.0.4 on 2024-04-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('owner', models.CharField(max_length=250)),
                ('model', models.IntegerField(null=True)),
            ],
        ),
    ]
