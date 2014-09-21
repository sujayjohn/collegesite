from django.db import models
from django.forms import ModelForm
from django.utils import timezone

from college.models import *


class doc_type(models.Model):
	def __unicode__(self):
		return self.name
	name=models.CharField(max_length=30)
	stage1=models.ForeignKey(userprofile,related_name='stage1',blank=True,null=True)
	stage2=models.ForeignKey(userprofile,related_name='stage2',blank=True,null=True)
	stage3=models.ForeignKey(userprofile,related_name='stage3',blank=True,null=True)
	stage4=models.ForeignKey(userprofile,related_name='stage4',blank=True,null=True)
	stage5=models.ForeignKey(userprofile,related_name='stage5',blank=True,null=True)
	stage6=models.ForeignKey(userprofile,related_name='stage6',blank=True,null=True)
	stage7=models.ForeignKey(userprofile,related_name='stage7',blank=True,null=True)
	stage8=models.ForeignKey(userprofile,related_name='stage8',blank=True,null=True)
	stage9=models.ForeignKey(userprofile,related_name='stage9',blank=True,null=True)
	stage10=models.ForeignKey(userprofile,related_name='stage10',blank=True,null=True)
	def stages(self):
		st=[]
		if self.stage1!=None:
			st.append(self.stage1)
		if self.stage2!=None:
			st.append(self.stage2)
		if self.stage3!=None:
			st.append(self.stage3)
		if self.stage4!=None:
			st.append(self.stage4)
		if self.stage5!=None:
			st.append(self.stage5)
		if self.stage6!=None:
			st.append(self.stage6)
		if self.stage7!=None:
			st.append(self.stage7)
		if self.stage8!=None:
			st.append(self.stage8)
		if self.stage9!=None:
			st.append(self.stage9)
		if self.stage10!=None:
			st.append(self.stage10)
		return st

class doctype_form(ModelForm):
	class Meta:
		model=doc_type
		fields=['name','stage1','stage2','stage3','stage4','stage5','stage6','stage7','stage8','stage9','stage10']
		
class doc(models.Model):
	def __unicode__(self):
		return str(self.id)+'   '+str(self.doctype)
	student=models.ForeignKey(student,related_name='student')
	doctype=models.ForeignKey(doc_type,related_name='doctype')
	location=models.ForeignKey(userprofile,related_name='location')
	stage_count=models.IntegerField(default=0)
	
	recieved_date_time=models.DateTimeField(default=timezone.now())
	completed_date_time=models.DateTimeField(blank=True,null=True)
	last_accessed=models.DateTimeField(auto_now=True)
	pickup_date_time=models.DateTimeField(blank=True,null=True)

	notes=models.CharField(max_length=200,blank=True)
	
	
	
	def addnote(self,new_note):
		self.notes+=' | '+new_note
		self.save()
	def ready(self):
		if self.completed_date_time!=None:
			return True
		return False
	def move(self):
		'''Moves the document to the next stage of processing'''
		stages=self.doctype.stages()
		current_pos=self.stage_count
		next_pos=current_pos+1
		
		if current_pos==(len(stages)-1):
			self.pickup_date_time=timezone.now()
			
		if next_pos in xrange(len(stages)):
			if next_pos==(len(stages)-1):
				self.completed_date_time=timezone.now()
			self.location=stages[next_pos]
			self.stage_count+=1
		self.save()
class doc_form(ModelForm):
	class Meta:
		model=doc
		fields=['doctype','student']
