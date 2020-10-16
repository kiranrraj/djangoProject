from django.db import models

# Customer Model
class Customer (models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Tag Model
class Tag (models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Product Model
class Product (models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, choices=CATEGORY)
    description = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.name} : Rs.{self.price}"


# Order Model
class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for deliery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
    status = models.CharField(max_length=200, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} : {self.date_created}"