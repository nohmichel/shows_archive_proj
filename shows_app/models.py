from django.db import models

class Shows(models.Model):
	title = models.CharField(max_length=45)
	network = models.CharField(max_length=45)
	release_date = models.DateField()
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __repr__(self):
		return f"<Shows object: {self.title} ({self.id})>"