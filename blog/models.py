from django.db import models

# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=250)
	slug=models.SlugField()
	intro=models.TextField()
	body=models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering=['-date_added']

class Comment(models.Model):
	post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
	name=models.CharField(max_length=250)
	email=models.EmailField()
	body=models.TextField()
	date_added=models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering=['date_added']
