# Generated by Django 4.0.5 on 2022-07-25 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_desc_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(default='sub', max_length=200),
        ),
    ]
