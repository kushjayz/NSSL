# Generated by Django 3.2.5 on 2022-09-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='venue',
            new_name='gohonzonVenue',
        ),
        migrations.AddField(
            model_name='member',
            name='gojukaiVenue',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
