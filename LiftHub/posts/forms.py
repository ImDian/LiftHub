from django import forms

from LiftHub.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['is_approved', 'user', 'has_been_edited']


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    class Meta:
        model = Post
        exclude = ['is_approved', 'user', 'image', 'has_been_edited']


class CommentBaseForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class CommentCreateForm(CommentBaseForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write your comment here...',
                'style': 'resize: none;',
            }),
        }


class CommentEditForm(CommentBaseForm):
    pass
