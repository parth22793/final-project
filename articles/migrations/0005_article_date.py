# Generated by Django 3.0.3 on 2020-04-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_brief'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.CharField(max_length=64, null=True, verbose_name='Publish date'),
        ),
    ]
