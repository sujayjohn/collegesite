from django.shortcuts import render

import college

def home(request,classid=None):
	'''
	renders attendence for selected class.
	'''
	data={}
	if classid:
		pass
	data['courses']=college.models.course.objects.all()	
	return render(request,'attendence/home.html',data)
