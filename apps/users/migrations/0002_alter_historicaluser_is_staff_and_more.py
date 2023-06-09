# Generated by Django 4.0 on 2023-03-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historicaluser',
            name='role',
            field=models.CharField(choices=[('regular', 'Regular'), ('admin', 'Admin')], default='regular', max_length=50, verbose_name='role'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('regular', 'Regular'), ('admin', 'Admin')], default='regular', max_length=50, verbose_name='role'),
        ),
    ]
