# Generated by Django 2.2.3 on 2019-09-17 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190917_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='semester',
            field=models.CharField(default='1', max_length=20),
            preserve_default=False,
        ),
    ]
