# Generated by Django 3.0.7 on 2020-09-20 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200920_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_url',
            field=models.CharField(default='https://www.kindpng.com/picc/m/24-248253_user-profile-default-image-png-clipart-png-download.png', max_length=200),
        ),
    ]
