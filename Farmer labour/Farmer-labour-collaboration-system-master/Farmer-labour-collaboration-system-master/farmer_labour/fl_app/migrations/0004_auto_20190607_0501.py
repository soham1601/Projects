# Generated by Django 2.0 on 2019-06-07 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fl_app', '0003_profile_fieldaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='FieldAddress',
            field=models.CharField(default='gjkg', max_length=300),
        ),
    ]
