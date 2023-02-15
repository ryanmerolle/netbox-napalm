# Generated by Django 4.1.5 on 2023-02-15 17:52

from django.db import migrations

def migrate_napalm(apps, schema_editor):
    Platform = apps.get_model('dcim', 'Platform')
    NapalmPlatform = apps.get_model('netbox_napalm_plugin', 'NapalmPlatform')
    qs = Platform.objects.all().exclude(napalm_driver__exact='')
    for platform in qs:
        NapalmPlatform.objects.create(
            platform=platform,
            napalm_driver=platform.napalm_driver,
            napalm_args=platform.napalm_args,
        )

class Migration(migrations.Migration):
    dependencies = [
        ("netbox_napalm_plugin", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(migrate_napalm),
    ]
