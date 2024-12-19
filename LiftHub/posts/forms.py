from django import forms

from LiftHub.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['is_approved', 'user', 'has_been_edited']


class PostCreateForm(PostBaseForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Write your post here...',
                'class': 'custom-textarea',
            }),
        }


class PostEditForm(PostBaseForm):
    class Meta:
        model = Post
        exclude = ['is_approved', 'user', 'image', 'has_been_edited']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 5,
                'class': 'custom-textarea',
            }),
        }


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
                'class': 'custom-textarea',
            }),
        }


class CommentEditForm(CommentBaseForm):
    pass
