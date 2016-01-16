from django.shortcuts import render, get_object_or_404, redirect          # add redirect
from django.utils import timezone
from .models import Post
from .forms import CommentForm 			# import the form we just created

def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

# Here we create our list view
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'post_list.html', {'posts': posts})

# Add our detail view here
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post_detail.html', {'post':post})

def add_comment_to_post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('myapp.views.post_detail', slug=post.slug)
	else:
		form = CommentForm()
	return render(request, 'add_comment_to_post.html', {'form': form})