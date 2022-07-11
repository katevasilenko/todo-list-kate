# Generated by Django 4.0.6 on 2022-07-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['is_done', 'datetime']},
        ),
        migrations.AddField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
