# Generated by Django 5.1.6 on 2025-02-24 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_project_developers_alter_project_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='Project_name',
        ),
    ]
