# Generated by Django 5.0.4 on 2024-04-15 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doingcard',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='donecard',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='todocard',
            old_name='name',
            new_name='title',
        ),
    ]
