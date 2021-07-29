from django.db import models

class Blog(models.Model):
	Author = models.CharField(max_length=15)
	Title = models.CharField(max_length=50)
	ThumbNail = models.ImageField(default='default.jpeg',blank=True)
	BlogField = models.TextField(max_length=10000)
	isPrivate = models.BooleanField()
	Date = models.DateField(auto_now=True)

	def __repr__(self):
		return self.Title
