from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Designer', 'Designer'),
        ('Customer', 'Customer'),
    )
    user_id = models.AutoField("User ID", primary_key=True, auto_created=True)
    avatar = models.ImageField("User Avatar", upload_to='avatars/', null=True, blank=True)
    gender = models.CharField("Gender", max_length=8, choices=GENDER, default='Male')
    role = models.CharField("User Type", max_length=10, choices=USER_TYPE, default='Customer')


class Product(models.Model):
    prod_ID = models.AutoField("Product ID", primary_key=True)
    prod_Name = models.CharField("Product Name", max_length=30, null=False)
    prod_Desc = models.CharField("Product Description", max_length=2000, null=False)
    prod_Price = models.IntegerField("Product Price/Piece", default=0.00)
    prod_img = models.ImageField("Product Image", upload_to='productImage/', null=True)

    def __str__(self):
        return f"{self.prod_ID}-->{self.prod_Name}"


class Packages(models.Model):
    package_ID = models.AutoField("Package ID", primary_key=True)
    package_Name = models.CharField("Package Name", max_length=30, null=False)
    attribute_values = models.CharField("Item Details JSON", max_length=200, null=False)
    package_Price = models.IntegerField("Package Price", null=False, default=0.00)
    prod_ID = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Product ID (FK)")


class Gallary(models.Model):
    img_id = models.AutoField("Image ID", primary_key=True)
    img_path = models.ImageField("Image Path", null=False, default="")
    upload_date = models.DateField("Image Upload Date", null=False, auto_now_add=True)


class Order(models.Model):
    order_id = models.AutoField("Order ID", primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name="Customer ID")
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, verbose_name="Product ID")
    quantity = models.ImageField('Product Quantity', max_length=10, default=500)
    attribute_value = models.CharField("Item Details JSON", max_length=2000, null=False)
    order_date = models.DateField("Order Date", auto_now_add=True, null=False)
    order_job_title = models.CharField("Name of Company/Business", max_length=100, null=False)
    order_desc = models.CharField("Details for Product", max_length=1000, null=False)
    product_img = models.ImageField("Template Image", null=False)
    address = models.CharField("Customer Address ", max_length=100, null=False)
    state = models.CharField("Customer State", max_length=30, null=False)
    city = models.CharField("Customer City", max_length=30, null=False)
    postal_code = models.IntegerField("Area Pin Code", null=False)


class FeedBack(models.Model):
    feedback_id = models.AutoField("FeedBack ID", primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name="Customer ID")
    feedback_desc = models.CharField("Customer FeedBack", max_length=300, null=False)
    feedback_date = models.DateField("FeedBack Date ", auto_now_add=True)


class Notification(models.Model):
    notify_id = models.AutoField(primary_key=True, auto_created=True)
    notify_detail = models.CharField("Notification Detail", max_length=200, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name="User ID")
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, verbose_name="Order ID")


class ImageTemplate(models.Model):
    temp_id = models.AutoField("Template ID", primary_key=True, auto_created=True)
    temp_img = models.ImageField("Template Image", null=False)


class Size(models.Model):
    size_id = models.AutoField("Size ID", primary_key=True, auto_created=True)
    prod_size = models.CharField("Product Size", max_length=20, null=False)

    def __str__(self):
        return f"{self.size_id}-->{self.prod_size}"


class Color(models.Model):
    color_id = models.AutoField("Color ID", primary_key=True, auto_created=True)
    prod_color = models.CharField("Product Color", max_length=50, null=False)

    def __str__(self):
        return f"{self.color_id}-->{self.prod_color}"


class PaperChoice(models.Model):
    paper_id = models.AutoField("Paper Choice ID", primary_key=True, auto_created=True)
    paper_choices_name = models.CharField("Paper Choices", max_length=50, null=False)

    def __str__(self):
        return f"{self.paper_id}-->{self.paper_choices_name}"


class ShrinkWrapping(models.Model):
    shrink_wrapping_id = models.AutoField("Shrink Wrapping ID", primary_key=True, auto_created=True)
    shrink_options = models.CharField("Shrink Wrap Options", max_length=20, null=False)

    def __str__(self):
        return f"{self.shrink_wrapping_id}-->{self.shrink_options}"


class AqutousCoating(models.Model):
    aqutous_coating_id = models.AutoField("Aqutous Coating ID", primary_key=True, auto_created=True)
    aqutous_coating_type = models.CharField("Aqutous Coating Type", max_length=30, null=False)

    def __str__(self):
        return f"{self.aqutous_coating_id}-->{self.aqutous_coating_type}"


class FoldingOptions(models.Model):
    folding_options_id = models.AutoField("Folding Options ID", primary_key=True, auto_created=True)
    folding_options_type = models.CharField("Folding Options Types", max_length=30, null=False)

    def __str__(self):
        return f"{self.folding_options_id}-->{self.folding_options_type}"


class NoOfMonths(models.Model):
    no_of_months_id = models.AutoField("No Of Months ID", primary_key=True, auto_created=True)
    months = models.CharField("No of Months", max_length=15, null=False)

    def __str__(self):
        return f"{self.no_of_months_id}-->{self.months}"


class HoleDrilling(models.Model):
    hole_drilling_id = models.AutoField("Hole Drilling ID", primary_key=True, auto_created=True)
    hole = models.BooleanField("Hole Drilling", null=False, default=False)

    def __str__(self):
        return f"{self.hole_drilling_id}-->{self.hole}"


class BindingMethod(models.Model):
    binding_method_id = models.AutoField("Binding Method ID", primary_key=True, auto_created=True)
    binding_methods = models.CharField("Binding Methods", max_length=30, null=False)

    def __str__(self):
        return f"{self.binding_method_id}-->{self.binding_methods}"


class ImageTemplateProductMapping(models.Model):
    imageTemp_p_map_id = models.AutoField("Template Image & Product Map ID", primary_key=True, auto_created=True)
    template_img_id = models.ForeignKey(ImageTemplate, null=False, on_delete=models.CASCADE,
                                        verbose_name="Image Template ID")
    prod_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, verbose_name="Product Id")


class SizeProductMapping(models.Model):
    size_p_map_id = models.AutoField("Size & Product Map ID", primary_key=True, auto_created=True)
    size_id = models.ForeignKey(Size, null=False, on_delete=models.CASCADE, verbose_name="Size ID")
    prod_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, verbose_name="Product Id")


class ColorProductMapping(models.Model):
    color_p_map_id = models.AutoField("Color & Product Map ID", primary_key=True, auto_created=True)
    color_id = models.ForeignKey(Color, null=False, on_delete=models.CASCADE, verbose_name="Color ID")
    prod_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, verbose_name="Product Id")


class PaperChoiceProductMapping(models.Model):
    paper_p_map_id = models.AutoField("Paper Choices & Product Map ID", primary_key=True, auto_created=True)
    paper_id = models.ForeignKey(PaperChoice, null=False, on_delete=models.CASCADE, verbose_name="Paper ID")
    prod_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, verbose_name="Product Id")


class ShrinkWrappingProductMapping(models.Model):
    shrink_wrap_p_map_id = models.AutoField("Shrink Wrapping & Product Map ID", primary_key=True, auto_created=True)
    shrink_wrapping_id = models.ForeignKey(ShrinkWrapping, null=False, on_delete=models.CASCADE,
                                           verbose_name="Shrink Wrapping ID")
    prod_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, verbose_name="Product Id")


class AqutousCoatingProductMapping(models.Model):
    aCoat_p_map_id = models.AutoField("Aqutous Coating & Product Map ID", primary_key=True, auto_created=True)
    aqutous_coating_id = models.ForeignKey(AqutousCoating, null=False, on_delete=models.CASCADE,
                                           verbose_name="Aqutous Coating ID")
    prod_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, verbose_name="Product Id")


class FoldingOptionsProductMapping(models.Model):
    folding_option_p_map_id = models.AutoField("Folding Options & Product Map ID", primary_key=True, auto_created=True)
    folding_options_id = models.ForeignKey(FoldingOptions, null=False, on_delete=models.CASCADE,
                                           verbose_name="Folding Options ID")
    prod_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, verbose_name="Product Id")


class NoOfMonthsProductMapping(models.Model):
    no_of_months_p_map_id = models.AutoField("No Of Months & Product Map ID", primary_key=True, auto_created=True)
    no_of_months_id = models.ForeignKey(NoOfMonths, null=False, on_delete=models.CASCADE,
                                        verbose_name="No Of Months ID")
    prod_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, verbose_name="Product Id")


class HoleDrillingProductMapping(models.Model):
    hole_drill_p_map_id = models.AutoField("Hole Drilling & Product Map ID", primary_key=True, auto_created=True)
    hole_drilling_id = models.ForeignKey(HoleDrilling, null=False, on_delete=models.CASCADE,
                                         verbose_name="Hole Drilling ID")
    prod_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, verbose_name="Product Id")


class BindingMethodProductMapping(models.Model):
    binding_methods_p_map_id = models.AutoField("Binding Method & Product Map ID", primary_key=True, auto_created=True)
    binding_method_id = models.ForeignKey(BindingMethod, null=False, on_delete=models.CASCADE,
                                          verbose_name="Binding Methods ID")
    prod_id = models.ForeignKey(Product, null=False, on_delete=models.CASCADE, verbose_name="Product Id")
