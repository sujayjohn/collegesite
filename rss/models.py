from django.db import models
from django.utils import timezone
from college.models import *
from django.forms import ModelForm

class teb_board(models.Model):
	def __unicode__(self):
		return str(self.heading)
	
	heading=models.CharField(max_length=50)
	pub_date=models.DateField('Publication Date',default=timezone.now())
	soc=models.ForeignKey(society,null=True,blank=True)
	description=models.CharField(max_length=800)
	author=models.ForeignKey(userprofile,related_name='author')
	approved=models.BooleanField(default=False)
	submission_date=models.DateField(default=timezone.now())
	
	def pretty_print(self):
		data={}
		data['Title']=self.heading
		data['Date']=str(self.pub_date.year)+'/'+str(self.pub_date.month)+'/'+str(self.pub_date.day)
		data['From']=self.soc.name
		data['Signed']=self.author.user.username
		data['Description']=self.description[:100]
		return data
	class Meta:
		permissions=(('can_approve_teb_board',"Can approve a Today's Engagement Board notice"),)
		
class teb_board_form(ModelForm):
	class Meta:
		model=teb_board
		fields=['heading','soc','description','pub_date']
