from django.db import models
from django.core.validators import FileExtensionValidator


# Database model for Books
class Books(models.Model):
	bookname = models.CharField(max_length=100)
	bookauthor = models.CharField(max_length=100)
	document = models.FileField(upload_to='books/', validators=[FileExtensionValidator(allowed_extensions=('pdf','docx','odt','pptx'))])
	uploaded_at = models.DateTimeField(auto_now_add=True)
	uploadedby = models.CharField(max_length=100)

	class Meta:
		ordering = ["-uploaded_at"]
		verbose_name = 'Books'
		verbose_name_plural = 'Books'
		
		""" To change table name in DB."""
		# db_table = 'BooksDB'  

	#Gives book name to the each row in admin
	def __str__(self):
		return self.bookname

	def delete(self,*args,**kwargs):
		self.document.delete()
		super().delete(*args,**kwargs)