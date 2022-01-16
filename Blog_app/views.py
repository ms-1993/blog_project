from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# Create your views here.
from Blog_app.forms import UserCreateForm


def register(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])

            login(request, new_user)
            return redirect('home')
    else:
        form = UserCreateForm()

    return render(request, 'Blog_app/blog_account/registration.html', {'form': form})


def login(request):
    return render(request, 'registration/login.html')


def forgot(request):
    return render(request, 'Blog_app/blog_account/forgotpassword.html')


def blog_list(request):
    return render(request, 'Blog_app/blog_post/blog-list.html')


def single_blog(request):
    return render(request, 'Blog_app/blog_post/blog-single.html')
