from django.db import models

# Create your models here.
class General(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
        verbose_name = 'General'
        verbose_name_plural = 'Generals'
        
class Page(General):
    title = models.CharField(verbose_name="عنوان", null=True, max_length=128)
    slug = models.CharField(verbose_name="پیوند یکتا", null=True, max_length=128)
    content = models.TextField(verbose_name="متن صفحه")
    
    class Meta:
        verbose_name = 'صفحه'
        verbose_name_plural = 'صفحات'