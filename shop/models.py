from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from main.models import General
# Create your models here.

class ProductCategory(General):
    name = models.CharField(verbose_name="نام دسته بندی محصول", null=True, max_length=128)
    slug = models.CharField(verbose_name="پیوند یکتا", null=True, max_length=128)
    thumbnail = models.ImageField(verbose_name="تصویر شاخص", upload_to="product/categroy/", null=True)
    
    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصولات'
        
class Product(General):
    title = models.CharField(verbose_name="عنوان", null=True, max_length=128)
    slug = models.CharField(verbose_name="پیوند یکتا", null=True, max_length=128)
    content = models.TextField(verbose_name="مشخصات")
    product_category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.CASCADE)
    thumbnail = models.ImageField(verbose_name="تصویر شاخص", upload_to="product/single/", null=True)
    
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        
class ProductGallery(General):
    product = models.ForeignKey(Product,blank=True, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="تصویر شاخص", upload_to="product/gallery/", null=True)
    
    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = "تصاویر گالری"