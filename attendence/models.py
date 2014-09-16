from django.db import models
from college import models as college_models
from django.utils import timezone



class month_total(models.Model):
	months_available=(
			(1,'January'),
			(2,'February'),
			(3,'March'),
			(4,'April'),
			(5,'May'),
			(6,'June'),
			(7,'July'),
			(8,'August'),
			(9,'September'),
			(10,'October'),
			(11,'November'),
			(12,'December')
			)
	month_name=models.IntegerField(choices=months_available)
	lecture=models.IntegerField(default=0)
	tutorial=models.IntegerField(default=0)
	practical=models.IntegerField(default=0)
	
class month_record(models.Model):

	months_available=(
		(1,'January'),
		(2,'February'),
		(3,'March'),
		(4,'April'),
		(5,'May'),
		(6,'June'),
		(7,'July'),
		(8,'August'),
		(9,'September'),
		(10,'October'),
		(11,'November'),
		(12,'December')
		)
	month_name=models.IntegerField(choices=months_available)
	lecture=models.IntegerField(default=0)
	tutorial=models.IntegerField(default=0)
	practical=models.IntegerField(default=0)
	
	adjust_lecture=models.IntegerField(default=0)
	adjust_tutorial=models.IntegerField(default=0)
	adjust_practical=models.IntegerField(default=0)

class student_attend(models.Model):
	def __unicode__(self):
		return self.student.name
	student=models.ForeignKey(college_models.student)
	
	month1=models.ForeignKey(month_record,null=True,blank=True,default=None,related_name='month1')
	month2=models.ForeignKey(month_record,null=True,blank=True,default=None,related_name='month2')
	month3=models.ForeignKey(month_record,null=True,blank=True,default=None,related_name='month3')
	month4=models.ForeignKey(month_record,null=True,blank=True,default=None,related_name='month4')
	month5=models.ForeignKey(month_record,null=True,blank=True,default=None,related_name='month5')
	month6=models.ForeignKey(month_record,null=True,blank=True,default=None,related_name='month6')
	
	
class student_group(models.Model):
	student1=models.ForeignKey(student_attend,null=True,blank=True,default=True,related_name='student1')
	student2=models.ForeignKey(student_attend,null=True,blank=True,default=True,related_name='student2')
	student3=models.ForeignKey(student_attend,null=True,blank=True,default=True,related_name='student3')
	student4=models.ForeignKey(student_attend,null=True,blank=True,default=True,related_name='student4')
	student5=models.ForeignKey(student_attend,null=True,blank=True,default=True,related_name='student5')
	student6=models.ForeignKey(student_attend,null=True,blank=True,default=True,related_name='student6')
	student7=models.ForeignKey(student_attend,null=True,blank=True,default=True,related_name='student7')
	student8=models.ForeignKey(student_attend,null=True,blank=True,default=True,related_name='student8')
	student9=models.ForeignKey(student_attend,null=True,blank=True,default=True,related_name='student9')
	student10=models.ForeignKey(student_attend,null=True,blank=True,default=True,related_name='student10')
	
class semester_attend(models.Model):
	def __unicode__(self):
		return self.paper
	paper=models.ForeignKey(college_models.course)
	date_from=models.DateField(default=timezone.now())
	date_upto=models.DateField(default=timezone.now())
	
	month_total_1=models.ForeignKey(month_total,null=True,blank=True,default=None,related_name='month_total_1')
	month_total_2=models.ForeignKey(month_total,null=True,blank=True,default=None,related_name='month_total_2')
	month_total_3=models.ForeignKey(month_total,null=True,blank=True,default=None,related_name='month_total_3')
	month_total_4=models.ForeignKey(month_total,null=True,blank=True,default=None,related_name='month_total_4')
	month_total_5=models.ForeignKey(month_total,null=True,blank=True,default=None,related_name='month_total_5')
	month_total_6=models.ForeignKey(month_total,null=True,blank=True,default=None,related_name='month_total_6')
	
	
	
	group1=models.ForeignKey(student_group,null=True,blank=True,default=True,related_name='group1')
	group2=models.ForeignKey(student_group,null=True,blank=True,default=True,related_name='group2')
	group3=models.ForeignKey(student_group,null=True,blank=True,default=True,related_name='group3')
	group4=models.ForeignKey(student_group,null=True,blank=True,default=True,related_name='group4')
	group5=models.ForeignKey(student_group,null=True,blank=True,default=True,related_name='group5')
	group6=models.ForeignKey(student_group,null=True,blank=True,default=True,related_name='group6')
	group7=models.ForeignKey(student_group,null=True,blank=True,default=True,related_name='group7')
	group8=models.ForeignKey(student_group,null=True,blank=True,default=True,related_name='group8')
	group9=models.ForeignKey(student_group,null=True,blank=True,default=True,related_name='group9')
	group10=models.ForeignKey(student_group,null=True,blank=True,default=True,related_name='group10')
	
