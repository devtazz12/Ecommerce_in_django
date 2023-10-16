from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class subcategory(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(category, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.category.name} - {self.name}"
    


class product(models.Model):
    name=models.CharField( max_length=100)
    subcategory=models.ForeignKey(subcategory, on_delete=models.CASCADE)
    discount=models.IntegerField()
    price=models.PositiveIntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to="images")
    quantity=models.IntegerField()
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name
    


class cart(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    prod= models.ForeignKey(product, on_delete=models.CASCADE)
    order_date_time = models.DateTimeField(auto_now_add=True)
    quantity= models.IntegerField(default=1)
    quantity_based_price=models.PositiveIntegerField()
    size= models.CharField(max_length=10, default="L")

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to="profile_pic",default="profile_img/user.jfif")
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.IntegerField( null=True)
    email = models.EmailField(max_length=254, unique=True, null=True)

    def __str__(self):
        return self.user.username
    
STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('On The Way', 'On The Way'),
        ('Completed', 'Completed'),
    ]

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    products= models.ManyToManyField('product')
    order_date= models.DateField(auto_now=True)
    total_amount=models.PositiveIntegerField(default=0)
    status= models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.user.username
    
    

    


    


    


