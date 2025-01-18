from django.db import models
from django.urls import reverse
# Create your models here.

class Page(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = 'PUBLISHED'
        DRAFT = 'DRAFT'
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def get_absolute_url(self):
        return reverse('page:page_detail', args=[self.slug])

    def __str__(self):
        return self.title

class ImagePageHeader(models.Model):
    image = models.ImageField(upload_to='images')
    alt_text = models.CharField(max_length=200)
    pages = models.ManyToManyField(Page, related_name='page_header_images')

    class Meta:
        verbose_name = 'Image Page Header'
        verbose_name_plural = 'Image Page Headers'

class BannerBlock(models.Model):
    class ImagePosition(models.TextChoices):
        LEFT = 'LEFT'
        RIGHT = 'RIGHT'
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images')
    alt_text = models.CharField(max_length=200)
    image_position = models.CharField(max_length=10, choices=ImagePosition.choices, default=ImagePosition.LEFT)
    pages = models.ManyToManyField(Page, related_name='banner_blocks')

    class Meta:
        verbose_name = 'Banner Block'
        verbose_name_plural = 'Banner Blocks'


class HomeBlock(models.Model):
    class HomeBlockType(models.TextChoices):
        BANNER = 'BANNER', 'Banner'
        IMAGE = 'IMAGE', 'Imagen'
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='images', verbose_name='Imagen')
    alt_text = models.CharField(max_length=200, verbose_name='Texto alternativo')
    block_type = models.CharField(max_length=10, choices=HomeBlockType.choices, default=HomeBlockType.BANNER, verbose_name='Tipo de bloque')
    order = models.PositiveIntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name = 'Bloque de Inicio'
        verbose_name_plural = 'Bloques de Inicio'
        ordering = ['order']

    def __str__(self):
        return f"{self.get_block_type_display()} - {self.title}"

class SliderBlock(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    pages = models.ManyToManyField(Page, related_name='slider_blocks')

    class Meta:
        verbose_name = 'Bloque de Slider'
        verbose_name_plural = 'Bloques de Slider'

    def __str__(self):
        return self.title

class SliderImage(models.Model):
    slider = models.ForeignKey(SliderBlock, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images', verbose_name='Imagen')
    alt_text = models.CharField(max_length=200, verbose_name='Texto alternativo')
    order = models.PositiveIntegerField(default=0, verbose_name='Orden')

    class Meta:
        verbose_name = 'Imagen de Slider'
        verbose_name_plural = 'Imágenes de Slider'
        ordering = ['order']

    def __str__(self):
        return f"Imagen {self.order} de {self.slider.title}"

class QuoteBlock(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(upload_to='images', verbose_name='Imagen')
    alt_text = models.CharField(max_length=200, verbose_name='Texto alternativo')
    pages = models.ManyToManyField(Page, related_name='quote_blocks')

    class Meta:
        verbose_name = 'Bloque de Quote'
        verbose_name_plural = 'Bloques de Quote'
