# Generated by Django 2.0 on 2019-06-06 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fl_app', '0002_auto_20190606_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='FieldAddress',
            field=models.CharField(default='', max_length=300),
        ),
    ]
