# Generated by Django 4.0.6 on 2022-08-23 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='meta_description',
            field=models.TextField(blank=True, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Title'),
        ),
    ]