# Generated by Django 3.0 on 2020-02-11 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200211_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(verbose_name={'cols': 15, 'rows': 4}),
        ),
    ]