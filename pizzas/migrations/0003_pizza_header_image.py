# Generated by Django 3.2 on 2021-05-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
