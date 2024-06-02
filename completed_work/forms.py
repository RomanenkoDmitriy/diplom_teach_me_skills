from django import forms

from completed_work.models import CommentsWork


class CommentsWorkForm(forms.ModelForm):

    class Meta:
        model = CommentsWork
        fields = ('comment',)
