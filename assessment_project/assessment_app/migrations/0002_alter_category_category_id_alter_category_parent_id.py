# Generated by Django 4.2.16 on 2024-10-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
