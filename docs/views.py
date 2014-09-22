from django.shortcuts import render,redirect
from django.http import HttpResponse

from docs.models import doc,doc_type,doc_form
from college.models import course,student,userprofile

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe,require_http_methods
import json

def home(request,docid=None):
	data={}
	if docid!=None:
		docid=int(docid)
		try:
			obj=doc.objects.get(id=docid)
			
		except Exception as e:
			data['error']='The document does not exist.'
		else:
			if obj.pickup_date_time!=None:
				data['error']='This document has been collected'
			data['result']=obj
				
	#office users go to office
	if request.user.is_authenticated() and request.user.is_active:
		if request.user.has_perm('docs.add_doc'):
			data['doc_add']=doc_form
		if request.user.has_perm('docs.change_doc'):
			data['docs_on_table']=doc.objects.filter(location=request.user.userprofile)
		
	return render(request,'docs/home.html',data)




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
				doc.objects.get(pk=int(i)).move()
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
