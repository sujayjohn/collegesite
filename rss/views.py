from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe,require_http_methods
from rss.models import notice as teb
from rss.models import notice_form
from django.utils import timezone
import datetime


def home(request):
	data={}
	if request.user.is_authenticated():
		if request.user.is_active:
			if request.user.has_perm('rss.add_notice'):
				data['teb_form']=notice_form	
			if request.user.has_perm('rss.can_approve_notice'):
				data['not_cleared']=teb.objects.filter(pub_date__gte=timezone.now()).filter(approved=False)
	now=timezone.now()
	one_month_back=datetime.datetime(now.date().year,now.date().month-1,now.date().day,now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
	notices=teb.objects.filter(pub_date__lte=timezone.now()).filter(pub_date__gte=one_month_back).filter(approved=True).order_by('-pub_date')
	dat=[]
	for i in notices:		
		dat.append(i.pretty_print())
	data['noticeboard']=notices
	
	return render(request,'rss/notice_board.html',data)
	
@login_required
@require_http_methods(['POST'])
def approve_notices(request):
	try:
		if request.user.is_authenticated():
			if request.user.is_active:
				if request.user.has_perm('rss.can_approve_notice'):
					not_cleared_notices=teb.objects.filter(approved=False).filter(pub_date__gte=timezone.now())
					post_keys=request.POST.keys()
					post_keys.remove('csrfmiddlewaretoken')
					for i in not_cleared_notices:
						if str(i.id) in post_keys:
							if request.POST[str(i.id)]=='on':
								i.approved=True
								i.save()
	except Exception as e:
		print e
	return redirect('news_home')
		
	
	
def notice(request,docid):
	data={}
	try:
		obj=teb.objects.get(id=int(docid))
	except Exception as e:
		print e
		data['notice']={'Notice ID ':'Not Available'}	
	else:
		data['notice']=obj.pretty_print()
	return render(request,'rss/notice.html',data)

@login_required
def add_new(request):
	if request.user.is_authenticated():
		if (not request.user.is_active)or(not request.user.has_perm('rss.add_notice')):
			return redirect('news_home')
	#user is now authentic
	form=notice_form(request.POST)# A form bound to the POST data
	if form.is_valid():# All validation rules pass
		# Process the data in form.cleaned_data
		# ...
		obj = form.save(commit=False)
		obj.author=request.user.userprofile
		obj.save()
	else:
		print 'form not valid>>>>>'
	return redirect('news_home')
