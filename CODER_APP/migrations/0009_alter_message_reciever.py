# Generated by Django 3.2.14 on 2022-08-13 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CODER_APP', '0008_auto_20220813_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reciever',
            field=models.CharField(max_length=50),
        ),
    ]
