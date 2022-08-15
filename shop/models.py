from distutils.command.upload import upload
from itertools import product
from tabnanny import verbose
from django.db import models
from main.models import General
from accounts.models import User
# Create your models here.

class ProductCategory(General):
    name = models.CharField(verbose_name="نام دسته بندی محصول", null=True, max_length=128)
    slug = models.CharField(verbose_name="پیوند یکتا", null=True, max_length=128)
    thumbnail = models.ImageField(verbose_name="تصویر شاخص", upload_to="product/categroy/", null=True)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'دسته بندی محصول'
        verbose_name_plural = 'دسته بندی محصولات'

class Size(models.Model):
    size_name = models.IntegerField(verbose_name="سایز")
    
    class Meta:
        verbose_name = 'سایز'
        verbose_name_plural = 'سایز‌ها'
    
    def __str__(self) -> str:
        return str(self.size_name)
        
class Product(General):
    title = models.CharField(verbose_name="عنوان", null=True, max_length=128)
    slug = models.CharField(verbose_name="پیوند یکتا", null=True, max_length=128)
    content = models.TextField(verbose_name="مشخصات")
    product_category = models.ForeignKey(ProductCategory, null=True, blank=True,related_name="categories", on_delete=models.CASCADE)
    product_size = models.ManyToManyField(Size, blank=True)
    thumbnail = models.ImageField(verbose_name="تصویر شاخص", upload_to="product/single/", null=True)
    is_discount = models.BooleanField(verbose_name="آیا تخفیف فعال است؟", default=False)
    price = models.CharField(verbose_name="قیمت اصلی", max_length=128, null=True)
    discount_price = models.CharField(verbose_name="قیمت تخفیف", max_length=127, null=True)
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        
    def get_final_price(self):
        if self.is_discount:
            return self.discount_price
        return self.price
        
class ProductGallery(General):
    product = models.ForeignKey(Product,blank=True, on_delete=models.CASCADE, related_name="image_gallery")
    image = models.ImageField(verbose_name="تصویر شاخص", upload_to="product/gallery/", null=True)
    
    def __str__(self) -> str:
        return str(self.id) + self.product.title
    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = "تصاویر گالری"
        
class Cart(General):
    user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,blank=True, on_delete=models.CASCADE)
    size = models.ForeignKey(Size,blank=True, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.user) + self.product.title + self.user.email
    
    class Meta:
        verbose_name = 'سبد خرید کاربر'
        verbose_name_plural = "سبد خرید کاربران"
        
class Checkout(General):
    status = models.CharField(verbose_name="وضعیت", max_length=128, null=True)
    products = models.ManyToManyField(Cart,blank=True)
    
    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = "سفارشات"