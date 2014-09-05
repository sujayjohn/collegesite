from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_safe,require_http_methods


from django.utils import timezone
import json

from roombook.models import *

def home(request):
	data={}
	print request.method
	data['reservation_form']=reservation_form
	data['time_stamp_value']=timezone.now()
	rms=room.objects.all()
	listed_rooms=[]
	for i in rms:
		x={}
		x['name']=i.name
		x['ac']=i.ac_available
		x['projector']=i.projector_available
		revs_available=i.get_reservations()
		revs_representation=[]
		#-------------------------------format the reservations
		for r in revs_available:
			tm_from={}
			tm_from['year']=r.time_from.date().year
			tm_from['month']=r.time_from.date().month
			tm_from['day']=r.time_from.date().day
			tm_from['hour']=r.time_from.time().hour
			tm_from['minute']=r.time_from.time().minute
			
			
			tm_to={}
			tm_to['year']=r.time_to.date().year
			tm_to['month']=r.time_to.date().month
			tm_to['day']=r.time_to.date().day
			tm_to['hour']=r.time_to.time().hour
			tm_to['minute']=r.time_to.time().minute
			
			by=r.booked_by.staff_adv1.name
			tm=[tm_from,tm_to,by]
			
			revs_representation.append(tm)
		#-------------------------------
		x['reservations']=revs_representation
		listed_rooms.append(x)
	if (request.user.has_perm('roombook.can_approve_reservation'))and(request.user.is_active):
		not_cleared_reservations=reservation.objects.filter(approved=False).filter(time_from__gte=timezone.now())
		data['not_cleared']=not_cleared_reservations
	data['room_data']=json.dumps(listed_rooms)
	return render(request,'roombook/home.html',data)

@login_required
@require_http_methods(['POST'])
def approve_reservations(request):
	if request.user.is_active:
		if request.user.has_perm('roombook.can_approve_reservation'):
			not_cleared_reservations=reservation.objects.filter(approved=False).filter(time_from__gte=timezone.now())
			post_keys=request.POST.keys()
			post_keys.remove('csrfmiddlewaretoken')
			for i in not_cleared_reservations:
				if str(i.id) in post_keys:
					if request.POST[str(i.id)]=='on':
						i.approved=True
						i.save()
	return redirect('roombook_home')


@login_required
@require_http_methods(['POST'])
def add_new(request):
	if (not request.user.has_perm('roombook.add_reservation'))or(not request.user.is_active):
		return redirect('roombook_home')
	#user is can add reservation
	form=reservation_form(request.POST)# A form bound to the POST data
	if form.is_valid():# All validation rules pass
		# Process the data in form.cleaned_data
		# ...
		room_booked=form.cleaned_data['room_booked']
		time_from=form.cleaned_data['time_from']
		time_to=form.cleaned_data['time_to']
	else:
		print 'form not valid>>>>>'
	
	#first check if it is allowed ie. booking is in future and not overlapping
	if not ((time_from<time_to) and (time_from>timezone.now())):
		print 'time is not correct'
	revs=room_booked.get_reservations()
	overlap_flag=False
	for i in revs:
		if(time_from>i.time_from)and(time_from<i.time_to):
			overlap_flag=True
			break
		if(i.time_from>time_from)and(i.time_from<time_to):
			overlap_flag=True
			break
		if(time_to>i.time_from)and(time_to<i.time_to):
			overlap_flag=True
			break
		if(i.time_to>time_from)and(i.time_to<time_to):
			overlap_flag=True
			break
	if not overlap_flag:
		obj = form.save(commit=False)
		obj.booked_by=request.user.userprofile
		obj.save()
	return redirect('roombook_home')
