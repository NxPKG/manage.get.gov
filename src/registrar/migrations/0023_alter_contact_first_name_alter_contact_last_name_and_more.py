# Generated by Django 4.2.1 on 2023-05-31 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registrar", "0022_draftdomain_domainapplication_approved_domain_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="first_name",
            field=models.TextField(
                blank=True,
                db_index=True,
                help_text="First name",
                null=True,
                verbose_name="first name / given name",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="last_name",
            field=models.TextField(
                blank=True,
                db_index=True,
                help_text="Last name",
                null=True,
                verbose_name="last name / family name",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="title",
            field=models.TextField(
                blank=True,
                help_text="Title",
                null=True,
                verbose_name="title or role in your organization",
            ),
        ),
    ]
