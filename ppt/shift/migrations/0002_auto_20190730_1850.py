# Generated by Django 2.2.3 on 2019-07-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shift', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='DEPT_SEC',
            field=models.CharField(max_length=50),
        ),
    ]