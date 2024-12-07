from django import forms

from LiftHub.posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['approved', 'user']


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass

