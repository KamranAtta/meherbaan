# Generated by Django 2.2 on 2019-04-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='ambition',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
