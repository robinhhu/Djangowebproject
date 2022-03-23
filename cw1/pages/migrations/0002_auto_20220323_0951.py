# Generated by Django 3.2.12 on 2022-03-23 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='p_code',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='module',
            unique_together={('m_code', 'm_name', 'm_year', 'm_semester')},
        ),
    ]