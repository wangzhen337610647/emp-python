# Generated by Django 2.0.7 on 2018-07-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_delete_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='hiredate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
