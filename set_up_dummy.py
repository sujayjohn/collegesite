#!/usr/bin/env python
import os
import sys
import random
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stephens.settings")


import college
import rss
import docs
import roombook

from django.contrib.auth.models import User,Group
from django.core.management import execute_from_command_line

execute_from_command_line(['manage.py','syncdb'])


groupnames=[{'name':'Administration',
		'permissions':['docs.change_doc','docs.add_doc']}
		,{'name':'Staff Advisor',
		'permissions':['roombook.add_reservation','rss.add_notice']},
		{'name':'Faculty',
		'permissions':[]}]
users=['staff_adv_1','staff_adv_2','office_window_1','office_window_2','office_inside_1','office_inside_2','notice_admin','registrar_of_soc']
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
departments=['Administration','Computer Science','Physics','Sports','English']
societies=['Computer Science Society','Alumni Cell','Bazam-e-Adab','The Chemistry Society','B.A. Society']
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
	a.save()
print 'Notifications added'


#make groups
for i in groupnames:
	g1=Group()
	g1.name=i['name']
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
	for i in xrange(int(random.random()*1000)):
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
a.purpose='General'
a.name='Phone'
a.value='+91-11-2766 7271 '
a.save()
a=college.models.contact()
a.purpose='Admission Help Line'
a.name='Phone'
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
for i in rooms:
	a=roombook.models.room()
	a.name=i
	a.ac_available=random.choice([True,False])
	a.projector_available=random.choice([True,False])
	a.save()
print 'rooms added'
print 'Please set user group permissions'
print 'Please assign users to groups'



