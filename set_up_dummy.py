#!/usr/bin/env python
import os
import sys
import random
import datetime
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stephens.settings")


import college
import rss
import docs
import roombook
import attendence

from django.contrib.auth.models import User,Group
from django.core.management import execute_from_command_line
from django.utils import timezone

execute_from_command_line(['manage.py','syncdb'])


groupnames=['Principal','Bursar','Dean(Residence)','Dean(Academic Affairs)','Chaplain','Public Information Officer','Special Assignments','Administration','Staff Advisor','Faculty']
users=['staff_adv_1','staff_adv_2','office_window_1','office_window_2','office_inside_1','office_inside_2','notice_admin','registrar_of_soc',
	'principal','bursar','seniortutor','dean(residence)','chaplain','dean(academic_affairs)','public_information_officer']
papers=[
	{'code':'MAPT-101','name':'Mathematics first year'},
	{'code':'PHPT-101','name':'Physics first year'},
	]
course_types=['UnderGraduate','PostGraduate','Vocational']
courses=[
	{'name':'B.Sc. Physical Science'},
	{'name':'B.Sc. Physics'},
	{'name':'B.A. Programme'},
	]
departments=['Administration','Computer Science','Physics','Sports','English','Principal Office']
societies=['Computer Science Society','Alumni Cell','Bazam-e-Adab','The Chemistry Society','B.A. Society','SUS','SSL']
students=['arjoonn sharma','gagan mahajan','karan jhunja','atima shahi']


quotes=['He who has failed has tried something greater...',
	'We have nothing to fear but fear itself...',
	'Ask and you are no longer a fool...',]
doctypes=['transcript','character_certificate','bonafide_certificate']
rooms=['A','B','C','U','R','Xc','Xd','OPLT','NPLT','PTR','CTR','Auditorium','Seminar Room','G','NCLT']

notifications=[
		'Dummy1','Dummy2','Dummy3','Dummy4','Dummy5','Dummy6','Dummy7','Dummy8','Dummy9','Dummy10',
		]
news=['Dummy news 1','Dummy news 2','Dummy news 3','Dummy news 4','Dummy news 6','Dummy news 7','Dummy news 8','Dummy news 9',]

print '===================================================='
print 'setting up dummy data'
print 'starting'

	

#make notifications
for i in notifications:
	a=college.models.custom_notice()
	a.title=i
	a.description=''
	alphabet='qwertyui  opasdfg   hjklzxcvbnm      '
	for i in xrange(int(random.random()*799)):
		a.description+=random.choice(alphabet)
	a.save()
print 'Notifications added'


#make groups
for i in groupnames:
	g1=Group()
	g1.name=i
	g1.save()
print 'Groups Added'
#add papers
for i in papers:
	a=college.models.paper()
	a.code=i['code']
	a.name=i['name']
	a.save()
print 'Papers Added'
#add course types
for i in course_types:
	a=college.models.course_type()
	a.name=i
	a.save()
print 'Course Type Added'
#add courses
for i in courses:
	a=college.models.course()
	a.name=i['name']
	a.type_of_course=random.choice(college.models.course_type.objects.all())
	a.save()
print 'Courses added'
#departments
for i in departments:
	a=college.models.department()
	a.name=i
	a.save()
print 'Departments Added'
#add societies
for i in societies:
	a=college.models.society()
	a.name=i
	a.save()
print 'Societies added'
#make users and userprofiles
for i in users:
	a=User()
	a.username=i
	a.set_password('asd')
	a.save()
	b=college.models.userprofile()
	b.user=a
	b.dept=random.choice(college.models.department.objects.all())
	if 'staff' in i:
		b.staff_adv1=random.choice(college.models.society.objects.all())
	b.save()
print 'Users added'


#make notices
for i in news:
	a=rss.models.notice()
	a.title=i
	a.description=''
	alphabet='qwertyui  opasdfg   hjklzxcvbnm      '
	for i in xrange(int(random.random()*799)):
		a.description+=random.choice(alphabet)
	x=college.models.userprofile.objects.all()
	a.author=random.choice(x)
	a.approved=True
	a.save()
print 'News added'



#make students
for i in students:
	a=college.models.student()
	a.name=i
	a.course=random.choice(college.models.course.objects.all())
	a.save()
print 'Students added'


#add a contact
a=college.models.contact()
a.name='Phone'
a.value='+91-11-2766 7271 '
a.save()
a=college.models.contact()
a.name='Admission Help Line'
a.value='011-27662168'
a.save()
print 'Contacts added'
#add quotes
for i in quotes:
	a=college.models.quote()
	a.value=i
	a.save()
print 'Quotes added'
#make doctypes
for i in doctypes:
	a=docs.models.doc_type()
	a.name=i
	a.stage1=random.choice(college.models.userprofile.objects.all())
	a.stage2=random.choice(college.models.userprofile.objects.all())
	a.stage3=random.choice(college.models.userprofile.objects.all())
	a.stage4=random.choice(college.models.userprofile.objects.all())
	a.save()
print 'Doc types Added'

#add dummy docs
for i in range(10):
	a=docs.models.doc()
	a.student=random.choice(college.models.student.objects.all())
	a.doctype=random.choice(docs.models.doc_type.objects.all())
	x=a.doctype.stages()
	a.stage_count=x.index(random.choice(x))
	a.location=x[a.stage_count]
	a.save()
print 'Docs added'

#add a few reservations
for i in range(20):
	a=roombook.models.reservation()
	a.booked_by=random.choice(college.models.userprofile.objects.all())
	a.room_booked=random.choice(roombook.models.room.objects.all())
	now=timezone.now()
	a.time_from=datetime.datetime(now.date().year,now.date().month,random.choice(range(1,21)),now.time().hour,now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
	now=a.time_from
	a.time_to=datetime.datetime(now.date().year,now.date().month,now.date().day,now.time().hour+random.choice((1,2,3)),now.time().minute,now.time().second,now.time().microsecond,now.tzinfo)
	a.approved=True;
	a.save()

for i in rooms:
	a=roombook.models.room()
	a.name=i
	a.ac_available=random.choice([True,False])
	a.projector_available=random.choice([True,False])
	a.save()
print 'rooms added'
print 'Please set user group permissions'
print 'Please assign users to groups'



