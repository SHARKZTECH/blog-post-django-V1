from django.shortcuts import render,redirect
from .models import Post
from .forms import CommentForm

# Create your views here.
def home(response):
	posts=Post.objects.all()
	return render(response,"index.html",{'posts':posts})

def details(response,slug):
	post=Post.objects.get(slug=slug)

	if response.method=="POST":
		form=CommentForm(response.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.post=post
			comment.save()

			return redirect('details',slug=post.slug)
	else:
		form=CommentForm()

	return render(response,"details.html",{'post':post,'form':form})

