from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe,require_http_methods
from rss.models import notice
from rss.models import notice_form
from django.utils import timezone
import datetime


def home(request):
	data={}
	if request.user.is_authenticated():
		if request.user.is_active:
			if request.user.has_perm('rss.add_notice'):
				data['notice_form']=notice_form	
			if request.user.has_perm('rss.change_notice'):
				data['not_cleared']=notice.objects.filter(pub_date__gte=timezone.now()).filter(approved=False).filter(alive=True)

	now=timezone.now()
	one_month_back=datetime.datetime(now.date().year,now.date().month-1,now.date().day,now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
	notices=notice.objects.filter(pub_date__lte=timezone.now()).filter(pub_date__gte=one_month_back).filter(approved=True).order_by('-pub_date','-id')
	data['noticeboard']=notices
	
	return render(request,'rss/notice_board.html',data)
	
@login_required
@require_http_methods(['POST'])
def approve_notices(request):

	try:
		if request.user.is_authenticated():
			if request.user.is_active:
				if request.user.has_perm('rss.change_notice'):
					not_cleared_notices=notice.objects.filter(approved=False).filter(pub_date__gte=timezone.now())
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
		
	
	
def notice_view(request,docid):
	data={}
	try:
		obj=notice.objects.get(id=int(docid))
	except Exception as e:
		print e
		data['notice']={'Notice ID ':'Not Available'}	
	else:
		data['notice']=obj
	return render(request,'rss/notice.html',data)

@login_required
def add_new(request):

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
		print 'form validation failed'
	return redirect('news_home')
