# Generated by Django 5.1.4 on 2024-12-15 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_rename_company_id_company_company_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employee",
            old_name="Company",
            new_name="company",
        ),
    ]