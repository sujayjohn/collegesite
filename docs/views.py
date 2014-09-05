from django.shortcuts import render,redirect
from django.http import HttpResponse

from docs.models import doc,doc_type,doc_form
from college.models import course,student,userprofile

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe,require_http_methods
import json

def home(request):
	data={}
	#office users go to office
	if request.user.is_authenticated():
		if request.user.is_active:
			if request.user.has_perm('docs.change_doc'):
				return redirect('docs_office')
	return render(request,'docs/home.html')

@require_safe#no post requests
def status(request,docid):
	data={}
	try:
		obj=doc.objects.get(id=int(docid))
	except Exception as e:
		print e
		data={'Error:  ':'This record does not exist'}
		data=json.dumps(data)
		return HttpResponse(data,content_type='application/json')
	else:
		data=obj.pretty_print()
		data=json.dumps(data)
		return HttpResponse(data,content_type='application/json')
		
@login_required	
def office(request):
	#only office users should be able to use
	if (not request.user.has_perm('docs.change_doc')) or (not request.user.is_active):
		return redirect(home)
	data={} 
	#=====================
	data['doc_form']=doc_form
	data['can_add_new_doc']=request.user.has_perm('docs.add_doc')
	#=====================
	dcs_tbl=doc.objects.filter(location=request.user.userprofile)
	d={}
	for i in dcs_tbl:
		if i.pickup_date_time==None:
			d[i.id]=i.student.name
	data['docs_on_table']=json.dumps(d)
	#=====================
	return render(request,'docs/office.html',data)
	
@login_required
@require_http_methods(['POST'])
def add(request):
	if (not request.user.has_perm('docs.add_doc')) or (not request.user.is_active):
		return redirect(office)
	form=doc_form(request.POST)# A form bound to the POST data
	if form.is_valid():# All validation rules pass
		# Process the data in form.cleaned_data
		# ...
		student_found=form.cleaned_data['student']
		doctype_found=form.cleaned_data['doctype']
		try:
			obj=doc()
			obj.student=student_found
			obj.doctype=doctype_found
			start=obj.doctype.stages()[0]
			obj.location=userprofile.objects.get(id=start)
			obj.save()
			return redirect('docs_newly_added',docid=obj.id)
		except Exception as e:
			print e
	return redirect(office)

@login_required
def newly_added(request,docid=None):
	data={}
	print request.method
	data['new_id']=docid
	return render(request,'docs/new.html',data)
	
@login_required
@require_http_methods(['POST'])
def edit(request):
	if not request.user.is_active:
		return redirect(office)
	try:
		data=request.POST['data']
		data=json.loads(data)
		#-------------------------------------------
		available=doc.objects.filter(location=request.user.userprofile)
		avl=[i.id for i in available]
		for i in data.keys():
			if int(i) in avl:
				doc.objects.get(id=int(i)).move()
		#-------------------------------------------
		data={'result':True}
		data=json.dumps(data)
		return redirect(office)
	except Exception as e:
		print e
	try:
		data=request.POST['edit']
		data=json.loads(data)
		#-------------------------------------------
		print data
		docid=data.keys()[0]
		obj=doc.objects.get(id=int(docid))
		if obj.location==request.user.userprofile:
			if obj.notes=='':
				obj.notes=str(data[docid])
			else:
				obj.addnote(data[docid])
			obj.save()
		#-------------------------------------------
		return redirect(office)
	except Exception as e:
		print e
