from django.contrib import admin
from docs.models import *

class doc_admin(admin.ModelAdmin):
	fields=['student','location','doctype','notes']
	
admin.site.register(doc,doc_admin)
admin.site.register(doc_type)
