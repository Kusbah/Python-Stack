# Generated by Django 5.2.1 on 2025-06-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default='old notes'),
            preserve_default=False,
        ),
    ]
