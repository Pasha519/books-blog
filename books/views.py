from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from books.models import Post,Category,Review,Contact
from django.contrib.auth import logout,login
from django.core.exceptions import MultipleObjectsReturned
from books import forms
from django.contrib import messages
from books.email_login import EmailLogin
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required


# Create your views here.
def post_list_view(request):
    rating = []
    if request.method =="POST":
        search = request.POST["search"]
        posts = Post.objects.filter(title__icontains=search)
        
        if not posts :
            messages.error(request, "Searched book doesn't exist")
        categories = Category.objects.all()
    else:
        posts = Post.objects.all()
        categories = Category.objects.all()

    for post in posts:
        count = Review.objects.filter(post=post).count()
        if count >5:
            rating.append(Review.objects.filter(post=post)[1])

    #pagination
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "books/books_list.html", {"post": posts, "categories": categories,"reviews":rating})

@login_required(login_url="/login")
def post_details_view(request,id=None):
    post = Post.objects.get(id=id)
    categories = Category.objects.all()
    if request.method =="POST":
        content = request.POST["content"]
        rating = request.POST["rating"]
        post_id = request.POST["post_id"]
        user = User.objects.get(id=request.user.id)
        post = Post.objects.get(id=post_id)

        review = Review(author=user,post=post,content=content,rating=rating)
        review.save()
    reviews = Review.objects.filter(post__id=post.id)
    return render(request, "books/books_details.html", {"post": post, "reviews": reviews,"categories":categories})

def category_post_view(request,id=None):
    categories = Category.objects.all()
    category = Category.objects.get(id=id)
    post1 = Post.objects.filter(category__id=category.id)
    
    rating = []
    posts = Post.objects.all()
    for post in posts:
        count = Review.objects.filter(post=post).count()
        if count > 5:
            rating.append(Review.objects.filter(post=post)[1])
    return render(request, "books/books_list.html", {"post": post1, "categories": categories, "reviews":rating})

def blog_logout_view(request):
    logout(request)
    return redirect("/blog")

def blog_login_view(request):
    form = forms.LoginPageForm()
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = EmailLogin.authenticate(request,username,password)
        if user is not None:
            login(request, user)
            return redirect("/blog")
        else:
            messages.error(request,"invalid email and password!!!")
    return render(request, "registration/login.html",{"form":form})


def blog_register_view(request):
    form = forms.RegisterPageForm()
    if request.method =="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        passowrd1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if passowrd1 and password2 and passowrd1 != password2:
            messages.error(request, "both passwords must be Same.!!")
            
        user = User(username=username,first_name=first_name,last_name=last_name,email=email,password=passowrd1)
        user.set_password(user.password)
        user.save()
        return redirect("/login")
    return render(request, "registration/register.html",{"form":form})


def blog_contact_view(request):
    form = forms.ContactForm()
    if request.method =="POST":
        phone = request.POST["phone"]
        email = request.POST["email"]
        desc = request.POST["desc"]
        user = User.objects.get(id=request.user.id)
        contact = Contact(user=user,phone=phone,email=email,desc=desc)
        contact.save()
        messages.success(request,"description submitted successfully..!")
    return render(request, "books/contact.html",{"form":form})
