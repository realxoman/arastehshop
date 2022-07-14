# Generated by Django 4.0.6 on 2022-07-14 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=128, null=True, verbose_name='عنوان')),
                ('slug', models.CharField(max_length=128, null=True, verbose_name='پیوند یکتا')),
                ('content', models.TextField(verbose_name='مشخصات')),
                ('thumbnail', models.ImageField(null=True, upload_to='product/single/', verbose_name='تصویر شاخص')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128, null=True, verbose_name='نام دسته بندی محصول')),
                ('slug', models.CharField(max_length=128, null=True, verbose_name='پیوند یکتا')),
                ('thumbnail', models.ImageField(null=True, upload_to='product/categroy/', verbose_name='تصویر شاخص')),
            ],
            options={
                'verbose_name': 'دسته بندی محصول',
                'verbose_name_plural': 'دسته بندی محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to='product/gallery/', verbose_name='تصویر شاخص')),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
            ],
            options={
                'verbose_name': 'تصویر گالری',
                'verbose_name_plural': 'تصاویر گالری',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.productcategory'),
        ),
    ]