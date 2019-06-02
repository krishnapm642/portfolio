from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

# Create your models here.


Users = get_user_model()
# Create your models here.
class Author(models.Model):

	user = models.OneToOneField(Users, on_delete = models.CASCADE)
	profilepic = models.ImageField(upload_to = 'imagesblog/')
	
	def __str__(self):
		return self.user.username

class Categories(models.Model):
	title = models.CharField(max_length = 100)

	def __str__(self):
		return self.title





class BlogPost(models.Model):
	title = models.CharField(max_length = 100)
	slug = models.SlugField(max_length = 250, null = True, blank = True)
	overview = models.TextField()
	content = HTMLField('Content')
	timestamp = models.DateTimeField(auto_now_add = True)
	view_count = models.IntegerField()
	comment_count = models.IntegerField()
	author = models.ForeignKey(Author, on_delete = models.CASCADE)
	thumbnail = models.ImageField(upload_to = 'blogimages/')
	categories = models.ManyToManyField(Categories)
	featured = models.BooleanField()
	previous_post = models.ForeignKey('self',related_name = 'previous',on_delete=models.SET_NULL, null = True, blank = True)
	next_post = models.ForeignKey('self',related_name = 'next',on_delete=models.SET_NULL, null = True, blank = True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post', kwargs = {
				'slug' : self.slug
			})


def pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug: 
		instance.slug = unique_slug_generator(instance) 

pre_save.connect(pre_save_receiver, sender = BlogPost) 