# Generated by Django 5.1.4 on 2024-12-14 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_employee"),
    ]

    operations = [
        migrations.RenameField(
            model_name="company",
            old_name="company_id",
            new_name="Company_id",
        ),
        migrations.RenameField(
            model_name="employee",
            old_name="company",
            new_name="Company",
        ),
    ]
