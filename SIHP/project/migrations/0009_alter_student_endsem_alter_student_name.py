# Generated by Django 4.2.5 on 2023-10-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_alter_student_predict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='endsem',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
