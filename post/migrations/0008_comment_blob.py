# Generated by Django 2.0.1 on 2018-01-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blob',
            field=models.TextField(default='hi'),
            preserve_default=False,
        ),
    ]
