from django.db import models
import datetime
from time import strftime

class ShowsManager(models.Manager):
	def basic_validator(self, postData):
		errors ={}

		if len(postData['title']) < 2:
			errors['title'] = "Title should be at least 2 characters."
		# show_title = Shows.objects['title']
		# if Shows.objects.filter(show_title = show_title).exists():
		# 	errors['title'] = "Title with this name already exists."

		if len(postData['network']) < 3:
			errors['network'] = "Network should be at least 3 characters."
		
		if len(postData['description']) > 0 and len(postData['description']) < 10:
			errors['description"'] = "Description should be at least 10 characters."

		today_check = datetime.datetime.now()		
		if 	postData['release_date'] > today_check.strftime("%Y-%m-%d"):
			errors["release_date"]  = "Release date must be in the past."

		return errors
	
class Shows(models.Model):
	title = models.CharField(max_length=45)
	network = models.CharField(max_length=45)
	release_date = models.DateField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	objects = ShowsManager()

	def __repr__(self):
		return f"<Shows object: {self.title} ({self.id})>"


