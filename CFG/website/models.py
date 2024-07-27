from django.db import models




class record2(models.Model):
	username=models.CharField(max_length=100,unique=True)
	role=models.CharField(max_length=100)


	def __str__(self):
		return self.username