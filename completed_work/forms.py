from django import forms

from completed_work.models import CommentsWork


class CommentsWorkForm(forms.ModelForm):
    class Meta:
        model = CommentsWork
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'styled-textarea', 'placeholder': 'Enter your comment...'}),
        }
