# Generated by Django 3.2.3 on 2021-06-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='article.Category', verbose_name='Kateqoriya'),
        ),
    ]
