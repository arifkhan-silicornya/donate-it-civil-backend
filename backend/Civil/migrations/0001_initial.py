# Generated by Django 3.2.12 on 2023-09-19 10:23

import Civil.OrderModel
import Civil.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Architecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('img', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to=Civil.models.upload_to_architecture)),
                ('price', models.CharField(max_length=300)),
                ('path', models.CharField(default='/', max_length=300)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BannerCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('img', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to=Civil.models.upload_to_banner)),
                ('path', models.CharField(default='/', max_length=300)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BottomBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=700)),
                ('img', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to=Civil.models.upload_to_bottom_banner)),
                ('link', models.TextField(blank=True, max_length=200, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_Name', models.CharField(max_length=200)),
                ('staff_title', models.CharField(max_length=200)),
                ('staff_img', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to=Civil.models.upload_to_Company)),
                ('email', models.EmailField(max_length=200)),
                ('mobileNumber', models.CharField(max_length=200)),
                ('home_address', models.TextField(blank=True, max_length=300)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=200)),
                ('phone_number', models.CharField(max_length=300)),
                ('Company_name', models.CharField(max_length=300)),
                ('website_url', models.CharField(max_length=300)),
                ('subject', models.CharField(max_length=300)),
                ('comment', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureWorksCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=300)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('office_address', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('contact_no', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noticeTitle', models.CharField(max_length=100)),
                ('file', models.FileField(blank=True, null=True, upload_to=Civil.models.upload_to_Notice)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=300)),
                ('project_description', models.TextField(max_length=300, null=True)),
                ('total_price', models.CharField(max_length=300, null=True)),
                ('total_online_paid', models.CharField(max_length=300, null=True)),
                ('status', models.CharField(choices=[('pen', 'Pending'), ('Pay', 'Payment'), ('can', 'Canceled'), ('wor', 'Working'), ('com', 'Completed'), ('del', 'Delivery')], default='pen', max_length=7)),
                ('delivery_date_from', models.DateField(null=True)),
                ('delivery_date_to', models.DateField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OurServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('icon', models.FileField(blank=True, null=True, upload_to=Civil.models.upload_to_service)),
                ('path', models.CharField(default='/', max_length=300)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Readmore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('img', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to=Civil.models.upload_to_readmore)),
                ('path', models.CharField(default='/', max_length=300)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaLinkCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_same', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=300, null=True)),
                ('link', models.CharField(max_length=300, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('OrderCivil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Civil.ordercivil')),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proName', models.CharField(max_length=100)),
                ('proDescription', models.TextField(blank=True, max_length=400)),
                ('proImg', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to=Civil.models.upload_to_product_img)),
                ('fileOne', models.FileField(blank=True, null=True, upload_to=Civil.models.upload_to_product)),
                ('fileTwo', models.FileField(blank=True, null=True, upload_to=Civil.models.upload_to_product)),
                ('fileThree', models.FileField(blank=True, null=True, upload_to=Civil.models.upload_to_product)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Civil.productcategorymodel')),
            ],
        ),
        migrations.CreateModel(
            name='PresentAddressCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_same', models.BooleanField(default=True)),
                ('country', models.CharField(max_length=300, null=True)),
                ('State', models.CharField(max_length=300, null=True)),
                ('city', models.CharField(max_length=300, null=True)),
                ('houseRoad', models.CharField(max_length=300, null=True)),
                ('zipCode', models.CharField(max_length=300, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('OrderCivil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Civil.ordercivil')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInfoCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_same', models.BooleanField(default=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=7, null=True)),
                ('title', models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Miss', 'Miss'), ('Dr', 'Dr'), ('Engr', 'Engr'), ('Master', 'Master')], max_length=7, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('occupation', models.CharField(blank=True, max_length=10, null=True)),
                ('first_name', models.CharField(max_length=300, null=True)),
                ('last_name', models.CharField(max_length=300, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('OrderCivil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Civil.ordercivil')),
            ],
        ),
        migrations.CreateModel(
            name='PermanentAddressCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_same_as_user', models.BooleanField(default=False)),
                ('is_same_present_address', models.BooleanField(default=False, null=True)),
                ('country', models.CharField(max_length=300, null=True)),
                ('State', models.CharField(max_length=300, null=True)),
                ('city', models.CharField(max_length=300, null=True)),
                ('houseRoad', models.CharField(max_length=300, null=True)),
                ('zipCode', models.CharField(max_length=300, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('OrderCivil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Civil.ordercivil')),
            ],
        ),
        migrations.CreateModel(
            name='OtherPdfCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=Civil.OrderModel.upload_to_OtherPdf)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('OrderCivil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Civil.ordercivil')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPdfCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=Civil.OrderModel.upload_to_OrderPdf)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('OrderCivil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Civil.ordercivil')),
            ],
        ),
        migrations.AddField(
            model_name='ordercivil',
            name='ProductCivil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Civil.productmodel'),
        ),
        migrations.AddField(
            model_name='ordercivil',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='FeatureWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True)),
                ('img', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[1920, 1080], upload_to=Civil.models.upload_to_feature_work)),
                ('path', models.CharField(default='/', max_length=300)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Civil.featureworkscategory')),
            ],
        ),
        migrations.CreateModel(
            name='Contact_infoCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_same', models.BooleanField(default=True)),
                ('personal_phone_dial_code', models.CharField(max_length=300, null=True)),
                ('personal_phone_number', models.CharField(max_length=300, null=True)),
                ('home_phone_dial_code', models.CharField(max_length=300, null=True)),
                ('home_phone_number', models.CharField(max_length=300, null=True)),
                ('contact_email', models.EmailField(max_length=300, null=True)),
                ('contact_address', models.TextField(max_length=300, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('OrderCivil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Civil.ordercivil')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyDetailCivil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_same', models.BooleanField(default=True)),
                ('Company_same', models.CharField(max_length=300)),
                ('Company_type', models.CharField(choices=[('Pr', 'Private'), ('Pu', 'Public'), ('O', 'Others')], max_length=7, null=True)),
                ('Company_location', models.CharField(max_length=300, null=True)),
                ('Company_website_url', models.URLField(max_length=300, null=True)),
                ('Company_phone_dial_code', models.CharField(max_length=300, null=True)),
                ('Company_phone_number', models.CharField(max_length=300, null=True)),
                ('Company_email', models.CharField(max_length=300, null=True)),
                ('Company_details', models.TextField(max_length=300, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('OrderCivil', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Civil.ordercivil')),
            ],
        ),
    ]
