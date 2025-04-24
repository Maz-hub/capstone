from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-input'}),
            'body': forms.Textarea(attrs={'placeholder': 'Your comment', 'rows': 4, 'class': 'form-textarea'}),
        }
