# Generated by Django 4.1.7 on 2023-02-28 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_fetcher', '0006_completedfetch_productlisting_delete_completed_fetch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlisting',
            name='timestamp_id',
        ),
        migrations.AddField(
            model_name='completedfetch',
            name='timestamp_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
