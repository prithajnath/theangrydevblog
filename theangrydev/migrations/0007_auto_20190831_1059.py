# Generated by Django 2.2.4 on 2019-08-31 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theangrydev', '0006_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='posts',
            field=models.ManyToManyField(related_name='tags', to='theangrydev.Post'),
        ),
    ]