from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 300)
	slug = models.TextField(unique = True)
	status = models.CharField(max_length= 50, blank = True,  choices = (('active','Active'),('','Default')))

	def __str__(self):
		return self.name

class SubCategory(models.Model):
	name = models.CharField(max_length = 300)
	slug = models.TextField(unique = True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	def __str__(self):
		return self.name


LABELS = (('offer','offer'), ('new','new'),('hot','hot'),('bigsale','bigsale'),('','default'))
class Product(models.Model):
	name = models.CharField(max_length = 500)
	slug = models.TextField(unique = True)
	image = models.ImageField(upload_to = 'media')
	price = models.IntegerField()
	discounted_price = models.IntegerField(default = 0)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	subcategory = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
	description = models.TextField(blank = True)
	status = models.CharField(max_length = 50, choices = (('active','active'),('','default')))
	labels = models.CharField(max_length = 500, choices = LABELS, blank = True)

	def __str__(self):
		return self.name


class Slider(models.Model):
	name = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	rank = models.IntegerField()
	status = models.CharField(max_length = 50, blank = True, choices = (('active','active'),('','default')))

	def __str__(self):
		return self.name


class Ad(models.Model):
	name = models.CharField(max_length = 300)
	image = models.ImageField(upload_to = 'media')
	link = models.URLField(max_length = 500, blank = True)
	rank = models.IntegerField()

	def __str__(self):
		return self.name


class Cart(models.Model):
	username = models.CharField(max_length = 400)
	slug = models.CharField(max_length = 500, unique = True)
	items = models.ForeignKey(Product, on_delete = models.CASCADE)
	quantity = models.IntegerField(default = 1)
	checkout = models.BooleanField(default = False)
	total = models.IntegerField(default = 1)

	def __str__(self):
		return self.username


class Contact(models.Model):
	name = models.CharField(max_length = 300)
	email = models.EmailField(max_length = 30)
	message = models.TextField()

	def __str__(self):
		return self.name

class Information(models.Model):
	address = models.CharField(max_length = 400)
	address_info = models.CharField(max_length = 500) 
	phone = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 50)

	def __str__(self):
		return f'{self.address} {self.phone}'


class CheckoutInfo(models.Model):
	address = models.CharField(max_length = 400)
	message = models.CharField(max_length = 800) 
	phone = models.CharField(max_length = 200)
	name = models.CharField(max_length = 200)
	lname = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 50)
	country = models.CharField(max_length = 500) 
	city = models.CharField(max_length = 200)

	def __str__(self):
		return f'{self.address} {self.phone}'


