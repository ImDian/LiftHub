from django import forms

from LiftHub.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['approved', 'user']


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CommentCreateForm(CommentBaseForm):
    pass


class CommentEditForm(CommentBaseForm):
    pass
