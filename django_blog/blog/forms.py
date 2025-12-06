from django import forms
from .models import Post, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas (e.g. django, blog, alx)"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            existing_tags = ", ".join(self.instance.tags.values_list('name', flat=True))
            self.fields['tags'].initial = existing_tags

    def save(self, commit=True):
        post = super().save(commit=False)

        if commit:
            post.save()

        tag_string = self.cleaned_data.get('tags', '')
        tag_names = [t.strip() for t in tag_string.split(',') if t.strip()]

        tag_objects = []
        for name in tag_names:
            tag_obj, created = Tag.objects.get_or_create(name=name)
            tag_objects.append(tag_obj)

        post.tags.set(tag_objects)

        return post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
