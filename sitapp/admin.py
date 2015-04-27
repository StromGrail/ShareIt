from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	fieldsets=[
		('User details',	{'fields':['uname','umail','upsswd']}),
		('Rating',	{'fields':['rating'],'classes':['collapse']}),

	]

	list_display=('uname','umail','rating')
	search_fields =['uname','umail','rating'] 

admin.site.register(User,UserAdmin)