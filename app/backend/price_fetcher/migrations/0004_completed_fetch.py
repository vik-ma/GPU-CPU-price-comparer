# Generated by Django 4.1.7 on 2023-02-26 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price_fetcher', '0003_product_listing_product_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Completed_Fetch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_list', models.TextField()),
                ('benchmark_type', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
