from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Page, ImagePageHeader, HomeBlock, SliderBlock, BannerBlock, SliderImage, QuoteBlock

class QuoteBlockInline(admin.StackedInline):
    model = QuoteBlock.pages.through
    extra = 1
    verbose_name = "Bloque de Quote"
    verbose_name_plural = "Bloques de Quote"
    autocomplete_fields = ['quoteblock']

class ImagePageHeaderInline(admin.StackedInline):
    model = ImagePageHeader.pages.through
    extra = 1
    verbose_name = "Imagen de Cabecera"
    verbose_name_plural = "Imágenes de Cabecera"
    autocomplete_fields = ['imagepageheader']

class SliderImageInline(admin.TabularInline):
    model = SliderImage
    extra = 1
    fields = ['image', 'admin_image', 'alt_text', 'order']
    readonly_fields = ['admin_image']
    ordering = ['order']

    def admin_image(self, obj):
        if obj and obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "No image"
    admin_image.short_description = 'Preview'

class SliderBlockInline(admin.StackedInline):
    model = SliderBlock.pages.through
    extra = 1
    verbose_name = "Bloque de Slider"
    verbose_name_plural = "Bloques de Slider"
    autocomplete_fields = ['sliderblock']

class BannerBlockInline(admin.StackedInline):
    model = BannerBlock.pages.through
    extra = 1
    verbose_name = "Bloque Banner"
    verbose_name_plural = "Bloques Banner"
    autocomplete_fields = ['bannerblock']

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'last_update', 'status']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImagePageHeaderInline, SliderBlockInline, BannerBlockInline, QuoteBlockInline]

@admin.register(HomeBlock)
class HomeBlockAdmin(admin.ModelAdmin):
    list_display = ['title', 'block_type', 'order', 'admin_image']
    list_filter = ['block_type']
    search_fields = ['title', 'content', 'alt_text']
    list_editable = ['order']
    ordering = ['order']
    list_per_page = 20
    readonly_fields = ['admin_image']
    fieldsets = (
        ('Main Information', {
            'fields': ('title', 'content')
        }),
        ('Image', {
            'fields': ('image', 'admin_image', 'alt_text')
        }),
        ('Settings', {
            'fields': ('block_type', 'order')
        }),
    )

    def admin_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "No image"
    admin_image.short_description = 'Preview'

@admin.register(ImagePageHeader)
class ImagePageHeaderAdmin(admin.ModelAdmin):
    list_display = ['alt_text', 'admin_image']
    search_fields = ['alt_text']
    exclude = ['pages']
    readonly_fields = ['admin_image']

    def admin_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "No image"
    admin_image.short_description = 'Preview'

@admin.register(SliderBlock)
class SliderBlockAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    exclude = ['pages']
    inlines = [SliderImageInline]

@admin.register(BannerBlock)
class BannerBlockAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_position', 'alt_text', 'admin_image']
    list_filter = ['image_position']
    search_fields = ['title', 'content', 'alt_text']
    exclude = ['pages']
    readonly_fields = ['admin_image']
    fieldsets = (
        ('Main Information', {
            'fields': ('title', 'content')
        }),
        ('Image', {
            'fields': ('image', 'admin_image', 'alt_text')
        }),
        ('Settings', {
            'fields': ('image_position',)
        }),
    )

    def admin_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "No image"
    admin_image.short_description = 'Preview'

@admin.register(QuoteBlock)
class QuoteBlockAdmin(admin.ModelAdmin):
    list_display = ['title', 'admin_image']
    search_fields = ['title']
    exclude = ['pages']
    readonly_fields = ['admin_image']

    def admin_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" />')
        return "No image"
    admin_image.short_description = 'Preview'
