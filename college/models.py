from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class document_link(models.Model):
	def __unicode__(self):
		return self.name
	name=models.CharField(max_length=100)
	list_doc=models.FileField(upload_to='files')

'''
<iframe src="http://docs.google.com/gview?url=http://path.com/to/your/pdf.pdf&embedded=true"style="width:600px; height:500px;" frameborder="0"></iframe>
'''
class client_data(models.Model):
	def __unicode__(self):
		return self.addr
	addr=models.GenericIPAddressField(primary_key=True)
	visits=models.IntegerField(default=0)
	agent=models.CharField(max_length=200)
	


class paper(models.Model):
	def __unicode__(self):
		return str(self.code)+str(self.name[:10])
	code=models.CharField(max_length=10)
	name=models.CharField(max_length=25)

class course_type(models.Model):
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=30)
	
	
class course(models.Model):
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=30)
	type_of_course=models.ForeignKey(course_type)
	
	paper1=models.ForeignKey(paper,related_name='paper1',blank=True,null=True)
	paper2=models.ForeignKey(paper,related_name='paper2',blank=True,null=True)
	paper3=models.ForeignKey(paper,related_name='paper3',blank=True,null=True)
	paper4=models.ForeignKey(paper,related_name='paper4',blank=True,null=True)
	paper5=models.ForeignKey(paper,related_name='paper5',blank=True,null=True)
	paper6=models.ForeignKey(paper,related_name='paper6',blank=True,null=True)
	paper7=models.ForeignKey(paper,related_name='paper7',blank=True,null=True)
	paper8=models.ForeignKey(paper,related_name='paper8',blank=True,null=True)
	paper9=models.ForeignKey(paper,related_name='paper9',blank=True,null=True)
	paper10=models.ForeignKey(paper,related_name='paper10',blank=True,null=True)
	paper11=models.ForeignKey(paper,related_name='paper11',blank=True,null=True)
	paper12=models.ForeignKey(paper,related_name='paper12',blank=True,null=True)
	paper13=models.ForeignKey(paper,related_name='paper13',blank=True,null=True)
	paper14=models.ForeignKey(paper,related_name='paper14',blank=True,null=True)
	
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
	dept=models.ForeignKey(department,related_name='dept')
	staff_adv1=models.ForeignKey(society,related_name='staff_adv1',blank=True,null=True)
	
	degree=models.CharField(max_length=100,blank=True)
	pg=models.CharField(max_length=100,blank=True)
	phd=models.CharField(max_length=100,blank=True)

class student(models.Model):
	def __unicode__(self):
		return str(self.name)
	name=models.CharField(max_length=40)
	course=models.ForeignKey(course,related_name='course')
	admission_date=models.DateField(default=timezone.now())
	
class contact(models.Model):
	def __unicode__(self):
		return self.purpose+'  -----  '+self.name+'  ----  '+self.value
	purpose=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	value=models.CharField(max_length=50)

class quote(models.Model):
	def __unicode__(self):
		return self.value[:20]
	value=models.CharField(max_length=50)
