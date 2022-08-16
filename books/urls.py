from django.urls import path
from books import views
urlpatterns = [
        path("blog/",views.post_list_view,name="books_blog"),
        path("<int:id>/details/",views.post_details_view,name="book_details"),
        path("<int:id>/category/",views.category_post_view,name="category_details"),
        path("logout/",views.blog_logout_view,name="logout"),
        path("login/",views.blog_login_view,name="login"),
        path("register/",views.blog_register_view,name="register"),
        path("contact/",views.blog_contact_view,name="contact")
]
