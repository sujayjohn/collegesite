from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from college.models import userprofile

class room(models.Model):
	def __unicode__(self):
		return self.name
	name=models.CharField(max_length=30)
	ac_available=models.BooleanField(default=False)
	projector_available=models.BooleanField(default=True)
	
	def get_reservations(self):
		revs=reservation.objects.filter(time_from__gte=timezone.now()).filter(room_booked=self).order_by('time_from').filter(approved=True)
		revs_avl=list(revs)
		return revs_avl
		
class room_form(ModelForm):
	class Meta:
		model=room
		fields=['name','ac_available','projector_available']
		
class reservation(models.Model):
	def __unicode__(self):
		return self.room_booked.name
		
	booked_by=models.ForeignKey(userprofile)
	room_booked=models.ForeignKey(room,related_name='room_booked')
	time_from=models.DateTimeField(default=timezone.now())
	time_to=models.DateTimeField(default=timezone.now())
	approved=models.BooleanField(default=False)
	
class reservation_form(ModelForm):
	class Meta:
		model=reservation
		fields=['room_booked','time_from','time_to']

