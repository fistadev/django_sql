# Generated by Django 4.0 on 2021-12-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_rename_uploaded_at_upload_upload_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genres', models.TextField(max_length=500)),
            ],
        ),
    ]
