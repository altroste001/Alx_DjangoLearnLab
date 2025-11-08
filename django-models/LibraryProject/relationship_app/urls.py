from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import books_list, ShowLibrary, RegisterView

urlpatterns = [
    path('', books_list, name='home'),
    path('books/', books_list, name='books_list'),
    path('library/<int:pk>/', ShowLibrary.as_view(), name='library_detail'),
    
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]