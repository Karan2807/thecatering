from django.db import models
class package(models.Model):
    package_id = models.AutoField   # Search on google = django model field reference.
    package_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="static/images", default="")

    def _str_(self):
        return self.package_name

class Contact(models.Model):
    msgid = models.AutoField(primary_key=True)   # Search on google = django model field reference.
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=50, default="")

    def _str_(self):
        return self.name


# class CartItem(models.Model):
#     product =models.ForeignKey(package)
#     quantity=models.IntegerField(default=1)
#     timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
#     updated=models.DateTimeField(auto_nowadd=False,auto_now=True)

#     def __unicode__(self):
#         return self.product.title

# class Cart(models.Model):
#     items=models.ManyToManyField(CartItem, null=True ,blank=True)
#     products=models.ManyToManyField(package,null=True,blank=True)
#     total=models.DecimalField(max_digits=100,decimal_places=2, default=0.00)
#     timestamp= models.DateTimeField(auto_now_add=True,auto_now=False)
#     updated=models.DateTimeField(auto_nowadd=False,auto_now=True)
#     active= models.BooleanField(default=True)

#     def __unicode__(self):
#         return "Cart id: %s" %(self.id)

