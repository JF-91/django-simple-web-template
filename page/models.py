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