# Generated by Django 3.0.5 on 2020-09-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200920_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='course',
            field=models.CharField(max_length=20, null=True),
        ),
    ]