# Generated by Django 2.2.24 on 2022-08-17 08:07
import phonenumbers
from django.db import migrations


def copy_phones_number_to_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    all_flats = Flat.objects.all()
    for flat in all_flats:
        flat.pure_phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
        flat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0007_flat_pure_phone'),
    ]

    operations = [
        migrations.RunPython(copy_phones_number_to_pure_phone)
    ]
