# Generated by Django 5.1.4 on 2025-01-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_alter_sliderblock_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoteBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='images', verbose_name='Imagen')),
                ('alt_text', models.CharField(max_length=200, verbose_name='Texto alternativo')),
                ('pages', models.ManyToManyField(related_name='quote_blocks', to='page.page')),
            ],
            options={
                'verbose_name': 'Bloque de Quote',
                'verbose_name_plural': 'Bloques de Quote',
            },
        ),
    ]