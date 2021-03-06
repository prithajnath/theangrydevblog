# Generated by Django 3.0.6 on 2020-06-09 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theangrydev', '0025_auto_20200609_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenttype',
            name='name',
            field=models.CharField(choices=[('TXT', 'Text'), ('CDE', 'Code'), ('IMG', 'Image'), ('QTE', 'Quote')], max_length=20),
        ),
        migrations.AlterField(
            model_name='vote',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='theangrydev.Post'),
        ),
    ]
