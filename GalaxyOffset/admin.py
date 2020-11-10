from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *


# Register your models here.

admin.site.unregister(Group)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Packages)
admin.site.register(Gallary)
admin.site.register(Order)
admin.site.register(FeedBack)
admin.site.register(Notification)
admin.site.register(ImageTemplate)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(PaperChoice)
admin.site.register(ShrinkWrapping)
admin.site.register(AqutousCoating)
admin.site.register(FoldingOptions)
admin.site.register(NoOfMonths)
admin.site.register(HoleDrilling)
admin.site.register(BindingMethod)
admin.site.register(ImageTemplateProductMapping)
admin.site.register(SizeProductMapping)
admin.site.register(ColorProductMapping)
admin.site.register(PaperChoiceProductMapping)
admin.site.register(ShrinkWrappingProductMapping)
admin.site.register(AqutousCoatingProductMapping)
admin.site.register(FoldingOptionsProductMapping)
admin.site.register(NoOfMonthsProductMapping)
admin.site.register(HoleDrillingProductMapping)
admin.site.register(BindingMethodProductMapping)
