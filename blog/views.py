from django.shortcuts import render, redirect
from .models import Post, Comment, Subcomment
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm, SubcommentForm


context={}

def home(request):
	context['order'] = 1
	if request.method == 'POST':
		name=request.POST.get('article')
		paint_posts=Post.objects.filter(painter=name).order_by('-date_posted')
		user=User.objects.filter(username=name).first()
		if paint_posts:
			posts=paint_posts
			context['posts']=posts
			context['name']=name
		elif user:
			posts=Post.objects.filter(author=user).order_by('-date_posted')
			context['posts']=posts
			context['name']=name
		else:
			context['posts']=None
			context['name']=name
	else:
		posts = Post.objects.order_by('-date_posted')
		context['posts'] = posts
		context['name'] = 'home'
	return render (request, 'blog/home.html', context)


def reverse(request, order, name):
	try:
		order = order + 1
		if name=='home':
			if order%2==0:
				posts = Post.objects.order_by('date_posted')
			else:
				posts = Post.objects.order_by('-date_posted')
			context['posts'] = posts
			context['name'] = 'home'
		else:
			paint_posts=Post.objects.filter(painter=name).order_by('-date_posted')
			user=User.objects.filter(username=name).first()
			if paint_posts:
				if order%2==0:
					posts=paint_posts.reverse()
				else:
					posts=paint_posts
				context['posts']=posts
				context['name']=name
			elif user:
				if order%2==0:
					posts=Post.objects.filter(author=user).order_by('date_posted')
				else:
					posts=Post.objects.filter(author=user).order_by('-date_posted')
				context['posts']=posts
				context['name']=name
			else:
				context['posts']=None
				context['name']=name
		context['order']=order
		return render (request, 'blog/home.html', context)
	except:
		return render (request, 'blog/home.html', context)


def about(request):
	return render (request, 'blog/about.html')


class PostDetailView(DetailView):
	model=Post 


class PostCreateView(LoginRequiredMixin, CreateView):
	model=Post 
	fields=['painting_name','painter','title','content','painting_image']

	def form_valid(self, form): 
		form.instance.author=self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView,):
	model=Post 
	fields=['painting_name','painter','title','content','painting_image']

	def form_valid(self, form): 
		form.instance.author=self.request.user
		return super().form_valid(form)

	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url='/'
	def test_func(self):
		post=self.get_object()
		if self.request.user==post.author:
			return True
		return False



def comment_create(request, post_id):
	model=Comment
	post=Post.objects.filter(id=post_id).first()
	author=request.user
	context={}
	context['post']=post
	context['author']=author
	if request.method == 'POST':
		content=request.POST['subject']
		comment=Comment(content=content, author=author, post=post)
		comment.save()
		return redirect('comment-detail')
	return render(request, 'blog/comment_form.html', context)


def comment_detail(request):
	context={}
	model=Comment
	comments=Comment.objects.order_by('-id')
	comment=comments.first()
	context['comment']=comment
	return render(request, 'blog/comment_detail.html', context)


def comment_update(request, comment_id):
	model=Comment
	comment=Comment.objects.filter(id=comment_id).first()
	post=comment.post
	author=request.user
	context={}
	context['post']=post
	context['author']=author
	if request.method == 'POST':
		comment.delete()
		content=request.POST['subject']
		comment=Comment(content=content, author=author, post=post)
		comment.save()
		return redirect('comment-detail')
	return render(request, 'blog/comment_form.html', context)


def comment_delete(request, comment_id):
	model=Comment
	comment=Comment.objects.filter(id=comment_id).first()
	comment.delete()
	return redirect('blog-home')


def subcomment_create(request, comment_id):
	model=Subcomment
	comment=Comment.objects.filter(id=comment_id).first()
	author=request.user
	context={}
	context['comment']=comment
	context['author']=author
	if request.method == 'POST':
		content=request.POST['subject']
		subcomment=Subcomment(content=content, author=author, comment=comment)
		subcomment.save()
		return redirect('subcomment-detail')
	return render(request, 'blog/subcomment_form.html', context)


def subcomment_detail(request):
	context={}
	model=Subcomment
	subcomments=Subcomment.objects.order_by('-id')
	subcomment=subcomments.first()
	context['subcomment']=subcomment
	return render(request, 'blog/subcomment_detail.html', context)


def subcomment_update(request, subcomment_id):
	model=Subcomment
	subcomment=Subcomment.objects.filter(id=subcomment_id).first()
	comment=subcomment.comment
	author=request.user
	context={}
	context['comment']=comment
	context['author']=author
	if request.method == 'POST':
		subcomment.delete()
		content=request.POST['subject']
		subcomment=Subomment(content=content, author=author, comment=comment)
		subcomment.save()
		return redirect('subcomment-detail')
	return render(request, 'blog/subcomment_form.html', context)


def subcomment_delete(request, subcomment_id):
	model=Subcomment
	subcomment=Subcomment.objects.filter(id=subcomment_id).first()
	subcomment.delete()
	return redirect('blog-home')