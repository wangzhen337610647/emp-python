# Generated by Django 2.0.7 on 2018-07-15 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_userinfo_nid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nid',
            field=models.IntegerField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
