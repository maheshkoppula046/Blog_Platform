from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, Comment
from .forms import CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'blog/logout.html')




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def home(request):
    posts = Post.objects.all().order_by('-created_at')  # Get all posts, ordered by most recent
    return render(request, 'blog/home.html', {'posts': posts})



def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Get the post by ID
    comments = Comment.objects.filter(post=post)  # Get all comments related to this post
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Link the comment to the post
            comment.save()
            return redirect('post_detail', post_id=post.id)  # Redirect to the same post page
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Handle file uploads (images)
        if form.is_valid():
            form.save()  # Save the new post to the database
            return redirect('home')  # Redirect to home page after saving
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})



@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)  # Bind the form with existing post
        if form.is_valid():
            form.save()  # Save the changes to the post
            return redirect('post_detail', post_id=post.id)  # Redirect to the post detail page
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})




def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post  # Associate the comment with the current post
            comment.save()
            return redirect('post_detail', post_id=post.id)  # Redirect to the post detail page
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})





