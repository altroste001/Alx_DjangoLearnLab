from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book
from .models import CustomUser


class BookAdmin(admin.ModelAdmin):
  
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)


class CustomUserAdmin(UserAdmin):
   
    
    model = CustomUser
    
    list_display = [
        'username', 
        'email', 
        'first_name', 
        'last_name', 
        'is_staff', 
        'date_of_birth'
    ]
    
    list_filter = [
        'is_staff', 
        'is_superuser', 
        'is_active', 
        'groups'
    ]
    
    search_fields = ['username', 'email', 'first_name', 'last_name']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )


admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)