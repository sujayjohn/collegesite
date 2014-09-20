from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils import timezone

import college
import attendence as attend

def home(request,classid=None):
	'''
	renders attendence for selected class.
	'''
	data={}
	data['url']=reverse("attend_home")
	data['courses']=college.models.course.objects.all()	
	if classid:
		try:
			c_id,s_id=map(int,classid.split('-'))
			cou=college.models.course.objects.get(pk=c_id)
			psp=college.models.paper.objects.filter(course=cou).filter(semester=s_id).distinct()
			pap_atd=attend.models.paper_attend.objects.filter(paper__in=psp).order_by('paper').distinct()
			
			att=attend.models.student_attend.objects.filter(paper_attend__in=pap_atd).order_by('student','paper_attend__paper')
			
			data['class_attend']=att
			data['paper_list']=pap_atd
		except Exception as e:
			print e
			data['error']=e
		
	return render(request,'attendence/home.html',data)
