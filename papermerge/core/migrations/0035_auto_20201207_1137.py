# Generated by Django 3.1.3 on 2020-12-07 10:37

from django.db import migrations, models
import django.db.models.deletion
import papermerge.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20201201_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basetreenode',
            name='title',
            field=models.CharField(max_length=200, validators=[papermerge.core.validators.safe_character_validator], verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='basetreenode',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='basetreenode',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='file_name',
            field=models.CharField(default='', max_length=1024, validators=[papermerge.core.validators.safe_character_validator]),
        ),
        migrations.AlterField(
            model_name='document',
            name='notes',
            field=models.TextField(blank=True, null=True, validators=[papermerge.core.validators.safe_character_validator], verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, validators=[papermerge.core.validators.safe_character_validator], verbose_name='name'),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('permissions', models.ManyToManyField(blank=True, to='auth.Permission', verbose_name='permissions')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, help_text='Determines what operations this user is authorized to perform.', null=True, on_delete=django.db.models.deletion.CASCADE, to='core.role', verbose_name='role'),
        ),
    ]
