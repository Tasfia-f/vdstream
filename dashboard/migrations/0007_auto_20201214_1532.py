# Generated by Django 3.1.4 on 2020-12-14 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_videoinfo_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoinfo',
            name='view',
            field=models.IntegerField(blank=True, default=0, null=0),
        ),
    ]
