# Generated by Django 4.2.5 on 2023-10-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_student_quiz2_student_quiz3_alter_student_endsem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='batch',
            field=models.CharField(default='00', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(default='satyam', max_length=1000),
        ),
    ]
