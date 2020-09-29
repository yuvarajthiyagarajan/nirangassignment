from django.shortcuts import render
from .models import Post

posts = [
	{
		'author': 'Yuvaraj Thiyagarajan',
		'title': 'Blog Post 1',
		'content': 'First Post content',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'TamilSelvan',
		'title': 'Blog Post 2',
		'content': 'Second Post content',
		'date_posted': 'April 21, 2018'
	}
]


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})