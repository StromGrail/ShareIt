from django.db import models

#Create database models ...raw structure of database

class User(models.Model):
	uname=models.CharField(max_length=500,primary_key=True)			#username
	upsswd=models.CharField(max_length=500)			#userpassword	
	umail=models.CharField(max_length=500)			#user mail
	rating=models.IntegerField(default=0)			#user's rating	as default=0
	
	def __str__(self):
		return self.uname