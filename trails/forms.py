from django import forms
from .models import Comment

# This form is used to create or update comments on trails
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'class': 'form-input'}),
            'text': forms.Textarea(attrs={'placeholder': 'Your comment', 'rows': 4, 'class': 'form-textarea'}),
        }
