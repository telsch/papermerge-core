# Generated by Django 3.2.9 on 2021-11-24 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20211112_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='document_version',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='core.documentversion'),
        ),
    ]