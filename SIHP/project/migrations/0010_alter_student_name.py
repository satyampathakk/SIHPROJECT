# Generated by Django 4.2.5 on 2023-10-12 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_student_endsem_alter_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]
