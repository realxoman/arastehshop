from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



#----------------------------- User ---------------------------------------
class User(AbstractUser):
    date_joined = models.DateTimeField(verbose_name="تاریخ عضویت", auto_now_add=True, null=True)
    last_update = models.DateTimeField(verbose_name="آخرین بروزرسانی", auto_now=True, null=True)
    last_login = models.DateTimeField(verbose_name="آخرین ورود", null=True, blank=True)
    
    is_manager = models.BooleanField(verbose_name="مدیر ارشد", default=False,\
        help_text="دسترسی کامل دارد.")
        
    phone = models.CharField(verbose_name="تلفن همراه", max_length=11, unique=True, null=True, blank=True, \
        help_text="همراه با صفر وارد شود.")

    email = models.EmailField(verbose_name="پست الکترونیکی", unique=True, null=True)

    REQUIRED_FIELDS = ['email']

    def get_date_joined(self):
        return self.date_joined.strftime("%H:%M - %Y/%m/%d")
    get_date_joined.short_description = 'تاریخ عضویت'

    def get_date_joined__date_only(self):
        return self.date_joined.strftime("%Y/%m/%d")

    def get_last_update(self):
        return self.last_update.strftime("%H:%M - %Y/%m/%d")
    get_last_update.short_description = 'آخرین بروزرسانی'

    def get_last_login(self):
        if self.last_login:
            return self.last_login.strftime("%H:%M - %Y/%m/%d")
        return "تاکنون وارد سایت نشده است."
    get_last_login.short_description = 'آخرین ورود'

    def __str__(self):
        if self.get_full_name():
            return "%s - %s" % (self.username, self.get_full_name())
        return "%s" % (self.username)

    class Meta:
        verbose_name_plural = '   کاربران'
        verbose_name = 'کاربر'