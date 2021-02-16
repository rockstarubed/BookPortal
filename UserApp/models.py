from django.db import models


#Database for Feedback
class FeedBack(models.Model):
	email = models.EmailField(max_length=100)
	message = models.CharField(max_length=100)

	class Meta(object):
		verbose_name = 'FeedBack'

	def __str__(self):
		return self.email
			
		
