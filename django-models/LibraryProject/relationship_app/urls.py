from django.urls import path
from django.contrib.auth import views as auth_views
from .views import books_list, ShowLibrary, register

urlpatterns = [
    path("", books_list, name="home"),
    path("books/", books_list, name="books_list"),
    path("library/<int:pk>/", ShowLibrary.as_view(), name="library_detail"),

    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", register, name="register"),
]
