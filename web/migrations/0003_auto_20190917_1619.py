# Generated by Django 2.2.3 on 2019-09-17 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0002_auto_20190718_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='items')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='1st', max_length=10)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('profilepicture', models.ImageField(blank=True, upload_to='profilePicture')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserAccount'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemImage',
            field=models.FileField(upload_to='items'),
        ),
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.UserAccount'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='images',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Item'),
        ),
    ]
