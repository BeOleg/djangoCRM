from django.db import models
from django.contrib.auth.models import User
# from django.conf import settings 
# Create your models here.
class UserInfo(models.Model):
	user = models.OneToOneField(User)
	site = models.URLField(blank=True)
	#image = models.imageField(blank=True)
	def __unicode__(self):
		return self.user.username

class Campaign(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=512, blank=True)
	view = models.CharField(max_length=50, blank=True)
	def __unicode__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=512, blank=True)
	def __unicode__(self):
		return self.name

class Lead(models.Model):
	campaign = models.ForeignKey(Campaign)
	product = models.ForeignKey(Product, null=True)
	product = models.ForeignKey(Product)
	campaign_url = models.CharField(max_length=100, null=True)
	phone = models.CharField(max_length=15)
	email = models.CharField(max_length=60)
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	city = models.CharField(max_length=50, null=True)
	comment = models.CharField(max_length=255, null=True)
	ip = models.CharField(max_length=30, null=True)
	agent = models.CharField(max_length=60, null=True)
	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

class LeadComment(models.Model):
	lead = models.ForeignKey(Lead)
	user = models.ForeignKey(User)
	title = models.CharField(max_length=512, null=False)
	comment = models.TextField(max_length=1024, null=False)
	time = models.DateTimeField(auto_now=True)
	# admin_id = models.ForeignKey(Users.user)

