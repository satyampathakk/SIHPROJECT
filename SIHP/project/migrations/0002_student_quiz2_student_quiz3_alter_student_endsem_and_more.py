# Generated by Django 4.2.5 on 2023-10-08 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='quiz2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='quiz3',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='endsem',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='preend',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='quiz1',
            field=models.IntegerField(default=0),
        ),
    ]