from django.db import models
from django.utils import timezone
from college.models import *
from django.forms import ModelForm

class notice(document):
	pub_date=models.DateField('Publication Date',default=timezone.now())
	soc=models.ForeignKey(society,null=True,blank=True)
	description=models.CharField(max_length=800)
	author=models.ForeignKey(userprofile,related_name='author')
	approved=models.BooleanField(default=False)
	submission_date=models.DateField(default=timezone.now())
	
	class Meta:
		permissions=(('can_approve_teb_board',"Can approve a Today's Engagement Board notice"),)
		
class notice_form(ModelForm):
	class Meta:
		model=notice
		fields=['title','soc','description','pub_date','associated_file']
