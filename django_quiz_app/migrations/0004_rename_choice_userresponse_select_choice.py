# Generated by Django 5.0.4 on 2024-04-14 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_quiz_app', '0003_userresponse'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userresponse',
            old_name='choice',
            new_name='select_choice',
        ),
    ]