# Generated by Django 4.0 on 2021-12-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0008_alter_bookscomplete_avg_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookscomplete',
            name='avg_rating',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='bookscomplete',
            name='num_pages',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bookscomplete',
            name='num_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bookscomplete',
            name='num_reviews',
            field=models.IntegerField(),
        ),
    ]
