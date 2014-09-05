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
			st.append(self.stage1.id)
		if self.stage2!=None:
			st.append(self.stage2.id)
		if self.stage3!=None:
			st.append(self.stage3.id)
		if self.stage4!=None:
			st.append(self.stage4.id)
		if self.stage5!=None:
			st.append(self.stage5.id)
		if self.stage6!=None:
			st.append(self.stage6.id)
		if self.stage7!=None:
			st.append(self.stage7.id)
		if self.stage8!=None:
			st.append(self.stage8.id)
		if self.stage9!=None:
			st.append(self.stage9.id)
		if self.stage10!=None:
			st.append(self.stage10.id)
		return st

class doctype_form(ModelForm):
	class Meta:
		model=doc_type
		fields=['name','stage1','stage2','stage3','stage4','stage5','stage6','stage7','stage8','stage9','stage10']
		
class doc(models.Model):
	def __unicode__(self):
		return str(self.id)
	student=models.ForeignKey(student,related_name='student')
	doctype=models.ForeignKey(doc_type,related_name='doctype')
	location=models.ForeignKey(userprofile,related_name='location')
	stage_count=models.IntegerField(default=0)
	
	recieved_date_time=models.DateTimeField(default=timezone.now())
	completed_date_time=models.DateTimeField(blank=True,null=True)
	last_accessed=models.DateTimeField(default=timezone.now())
	pickup_date_time=models.DateTimeField(blank=True,null=True)

	notes=models.CharField(max_length=150,blank=True)
	
	
	def pretty_print(self):
		'''pretty prints the data in the database'''
		data={}
		data['Student']=self.student.name
		
		data['Last Accessed']=str(self.last_accessed.year)+'/'+str(self.last_accessed.month)+'/'+str(self.last_accessed.day)+'        '+str(self.last_accessed.hour)+':'+str(self.last_accessed.minute)+'  HRS'
		if self.pickup_date_time==None:
			data['Location']=self.location.user.username+ ' -  '+self.location.dept.name
			if self.completed_date_time!=None:
				data['Action']='Ready for Pickup'
			else:
				if self.notes!='':
					data['Action']=self.notes.split('|')[-1]
		else:
			data['Action']='Document has been picked up'
			data['Pickup Date']=str(self.pickup_date_time.year)+'/'+str(self.pickup_date_time.month)+'/'+str(self.pickup_date_time.day)+'        '+str(self.pickup_date_time.hour)+':'+str(self.pickup_date_time.minute)+'  HRS'
			data.pop('Last Accessed')
		return data
	def addnote(self,new_note):
		self.notes+=' | '+new_note
		self.save()
	
	def move(self):
		'''Moves the document to the next stage of processing'''
		stages=self.doctype.stages()
		current_pos=self.stage_count
		next_pos=current_pos+1
		
		if current_pos==(len(stages)-1):
			self.pickup_date_time=timezone.now()
			self.last_accessed=timezone.now()
			
		if next_pos in xrange(len(stages)):
			if next_pos==(len(stages)-1):
				self.completed_date_time=timezone.now()
			self.last_accessed=timezone.now()
			self.location=userprofile.objects.get(id=stages[next_pos])
			self.stage_count+=1
		self.save()
class doc_form(ModelForm):
	class Meta:
		model=doc
		fields=['doctype','student']
