# Generated by Django 4.1.7 on 2023-02-28 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_fetcher', '0010_remove_completedfetch_timestamp_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedfetch',
            name='timestamp_id',
            field=models.CharField(default='', max_length=26),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productlisting',
            name='timestamp_id',
            field=models.CharField(default='', max_length=26),
            preserve_default=False,
        ),
    ]