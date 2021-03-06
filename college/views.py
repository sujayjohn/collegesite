from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import Group
import datetime
import os
import college.models as college_models
from rss.models import *
import random

def document(request,docid):
	data={}
	try:
		d=college_models.document.objects.get(id=docid)
		if d.alive==True:
			data['document']=d
		else:
			print 'Document is not alive.'
	except Exception as e:
		try:
			d=college_models.custom_notice.objects.get(id=docid)
			if d.alive==True:
				data['document']=d
			else:
				print 'Document is not alive.'
		except Exception as et:
			print 'Document with ID',docid,' does not exist'
			print e
			print et
	return render(request,'college/doc_viewer.html',data)

def home(request):
	'''returns the home page'''
	#record the client data
	client_addr=request.META['REMOTE_ADDR']
	client_browser=request.META['HTTP_USER_AGENT']
	try:
		ob=college_models.client_data.objects.get(addr=client_addr)
	except:
		ob=college_models.client_data()
		ob.addr=client_addr
		ob.agent=client_browser
		ob.save()
	else:
		ob.visits+=1
		if ob.agent!=client_browser:
			ob.agent=client_browser
		ob.save()
	#now respond to request
	data={}
	here=os.getcwd()
	
	path=os.path.join(here,'college','static','college','images','homepage')
	data['picture_gallery']=os.listdir(path)
	try:
		data['quote_of_the_day']=random.choice(college_models.quote.objects.all())
	except Exception as e:
		print e
	
	now=timezone.now()
	one_month_back=datetime.datetime(now.date().year,now.date().month-1,now.date().day,now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
	notices=notice.objects.filter(pub_date__lte=timezone.now()).filter(pub_date__gte=one_month_back).filter(approved=True).filter(alive=True).order_by('-pub_date','-id')[:5]
	data['news']=notices

	lists=college_models.custom_notice.objects.filter(alive=True).filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
	data['notifications']=lists
	principal_list=college_models.principal_desk.objects.filter(alive=True).filter(pub_date__lte=timezone.now()).order_by('-pub_date','-id')[:5]
	data['principal_desk']=principal_list
	
	return render(request,'college/home.html',data)

def alumni(request):
	data={}
	return render(request,'college/alumni_home.html',data)
def clg_admin(request):
	data={}
	grps=Group.objects.order_by('id')
	d=[]
	for i in grps:
		people=i.user_set.all()
		
		x=[i for i in people if i.is_active()]
		d.append({'name':i.name,'members':x})
	data['administration_categories']=d
	return render(request,'college/clg_admin.html',data)
	
def notification_view(request,docid=None):	
	data={}
	if docid!=None:
		try:
			obj=college_models.custom_notice.objects.get(id=int(docid))
		except Exception as e:
			print e
			data['notice']={'title':'Not Available','description':'This notification does not exist.','pub_date':None}	
		else:
			if obj.alive:
				data['notice']=obj
			else:
				data['notice']={'title':'Not Available','description':'This notification has been removed.','pub_date':None}	
	else:
		notifications=college_models.custom_notice.objects.filter(pub_date__lte=timezone.now()).filter(alive=True).order_by('-pub_date','-id')
		data['notifications']=list(notifications)
	return render(request,'college/notifications_view.html',data)
	
	
def archive(request):
	data={}
	return render(request,'college/archive_home.html',data)
def society(request,soc_name=None):
	data={}
	if soc_name==None:
		soc_list=college_models.society.objects.all()
		data['society_list']=[{'name':i.name,'urlname':i.name.replace(' ','').lower()} for i in soc_list]
		return render(request,'college/society_home.html',data)
	else:
		try:
			temp=college_models.society.objects.all()
			temp2=[i.name for i in temp if i.name.replace(' ','').lower()==soc_name.strip().lower()]
			temp2=temp2[0]
			data['soc_page']=temp2
			
			
			template_name='college/society/'+soc_name.replace(' ','').lower()+'.html'
			return render(request,template_name,data)
		except Exception as e:
			print e
			soc_list=college_models.society.objects.all()
			data.pop('soc_page')
			data['society_list']=[{'name':i.name,'urlname':i.name.replace(' ','').lower()} for i in soc_list]
			return render(request,'college/society_home.html',data)
def events(request):
	data={}
	return render(request,'college/events_home.html',data)		
def department(request,dept_name=None):
	data={}
	dept_list=college_models.department.objects.all()
	if dept_name==None:
		data['department_list']=[{'name':i.name,'urlname':i.name.replace(' ','').lower()} for i in dept_list]
		return render(request,'college/department_home.html',data)
	else:
		try:
			temp=college_models.department.objects.all()
			temp2=[i.name for i in temp if i.name.replace(' ','').lower()==dept_name.strip().lower()]
			temp2=temp2[0]
			data['dept_page']=temp2
			
			template_name='college/department/'+dept_name.replace(' ','').lower()+'.html'
			return render(request,'college/department/'+dept_name+'.html',data)
		except Exception as e:
			print e
			data.pop('dept_page')
			data['department_list']=[{'name':i.name,'urlname':i.name.replace(' ','').lower()} for i in dept_list]
			return render(request,'college/department_home.html',data)
def principal(request,docid=None):
	data={}
	if docid!=None:
		try:
			obj=college_models.principal_desk.objects.get(id=int(docid))
		except Exception as e:
			print e
			data['notice']={'title':'Not Available','description':'This document does not exist.','pub_date':None}	
		else:
			if obj.alive:
				data['notice']=obj
			else:
				data['notice']={'title':'Not Available','description':'This document has been removed.','pub_date':None}	
	else:
		docs=college_models.principal_desk.objects.filter(alive=True).filter(pub_date__lte=timezone.now()).order_by('-pub_date','-id')
		data['principal_desk_docs']=docs
	return render(request,'college/principal_home.html',data)
def contact_us(request):
	data={}
	data['contacts']=college_models.contact.objects.all()
	return render(request,'college/contact_us.html',data)
	
def academics_home(request):
	data={}
	
	return render(request,'college/academics_home.html',data)
def admissions_home(request):
	data={}
	
	return render(request,'college/admissions_home.html',data)
