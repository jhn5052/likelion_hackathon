# Generated by Django 2.2.3 on 2019-08-07 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0022_auto_20190805_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='File',
            field=models.FileField(null=True, upload_to='board/'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateField(default=datetime.date(2019, 8, 7)),
        ),
    ]
