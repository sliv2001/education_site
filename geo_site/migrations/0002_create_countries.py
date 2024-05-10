"""
The module contains Django migration for database of countries.
"""
from django.db import migrations
from ..models import Country, Region

def fill_countries(apps, schema_editor):
    """
    Fills tables of countries and regions with data from CSV file.
    """
    entries = []
    regions = []
    with open('./geo_site/data/capitals.csv', encoding='UTF-8') as fin:
        for line in fin.readlines()[1:]:
            country, capital, region = line.split(',')[3:6]
            if not region in regions:
                regions.append(region)
                region_entry = Region.objects.create(name=region)
            else:
                region_entry = Region.objects.get(name=region)
            if capital != '':
                entries.append(Country(region=region_entry, name=country, capital=capital))
    Country.objects.bulk_create(entries)

class Migration(migrations.Migration):
    """
    The class defines migration for countries and regions database.
    """
    dependencies = [
        ("geo_site", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(fill_countries),
    ]
