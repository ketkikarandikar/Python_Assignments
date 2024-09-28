from django.db import models

# Create your models here.
class Postlist (models.Model):
	post_id=models.IntegerField()
	id=models.IntegerField(primary_key=True)
	title=models.CharField(max_length=100,blank=True)
	content = models.CharField(max_length=100,blank=True)
	created_at=models.CharField(max_length=100,blank=True)
	updated_at=models.CharField(max_length=100,blank=True)
	def __str__(self):
		return self.title