from django.db import models
from django.utils import timezone

# Create your models here.
class CounselCenter(models.Model):
	title = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	telno = models.CharField(max_length=20)

	description = models.TextField()
	imported_date = models.DateTimeField(default=timezone.now)

	def imported(self):
		self.imported_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class UnivCounselingCenter(models.Model):
	title = models.CharField('센터명', max_length=100)
	manager = models.CharField('관리자', max_length=50)
	telno = models.CharField('전화번호', max_length=20)
	email = models.CharField('Email', max_length=100)
	address = models.CharField('주소', max_length=200)
	webSite = models.URLField(blank=True)
	#title,manager,tel,email,address