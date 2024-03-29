# Generated by Django 4.1 on 2024-01-19 12:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Blog.comment'),
        ),
    ]
