from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime



class document(models.Model):
	def __unicode__(self):
		return self.title
	title=models.CharField(max_length=100)
	associated_file=models.FileField(upload_to='files',blank=True,null=True,default=None)
	alive=models.BooleanField(default=True)


class custom_notice(document):
	description=models.CharField(max_length=800)
	pub_date=models.DateTimeField(default=timezone.now())
	def recent(self):
		now=timezone.now()
		one_month_back=datetime.datetime(now.date().year,now.date().month-1,now.date().day,now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
		if now>one_month_back:
			return True
		return False
		
class client_data(models.Model):
	def __unicode__(self):
		return self.addr
	addr=models.GenericIPAddressField(primary_key=True)
	visits=models.IntegerField(default=0)
	agent=models.CharField(max_length=200)
	



class course_type(models.Model):
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=30)
	
	
class course(models.Model):
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=30)
	type_of_course=models.ForeignKey(course_type)

class paper(models.Model):
	def __unicode__(self):
		return self.code
	code=models.CharField(max_length=10)
	name=models.CharField(max_length=25)
	course=models.ForeignKey(course)
	semester=models.IntegerField(default=0)	

class department(models.Model):
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=35)
	
	
class society(models.Model):
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=70)
	
class userprofile(models.Model):
	def __unicode__(self):
		return str(self.user.username)
	user=models.OneToOneField(User)
	title=models.CharField(max_length=15,blank=True,null=True,default=None)
	picture=models.ImageField(upload_to='files/userpics',blank=True,null=True,default=None)
	
	dept=models.ForeignKey(department,related_name='dept')
	staff_adv1=models.ForeignKey(society,related_name='staff_adv1',blank=True,null=True)
	
	degree=models.CharField(max_length=100,blank=True)
	pg=models.CharField(max_length=100,blank=True)
	phd=models.CharField(max_length=100,blank=True)

class student(models.Model):
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=40)
	picture=models.ImageField(upload_to='files/studentpics',blank=True,null=True,default=None)
	email=models.EmailField(null=True,blank=True,default=None)
	
	
	course=models.ForeignKey(course,related_name='course')
	admission_date=models.DateField(default=timezone.now())
	
class contact(models.Model):
	def __unicode__(self):
		return self.name+'  ----  '+self.value
	name=models.CharField(max_length=50)
	value=models.CharField(max_length=50)

class quote(models.Model):
	def __unicode__(self):
		return self.value[:20]
	value=models.CharField(max_length=50)

