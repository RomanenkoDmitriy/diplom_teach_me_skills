from django.forms import ModelForm

from completed_work.models import CompletedWork


class CompletedWorkForm(ModelForm):
    class Meta:
        model = CompletedWork
        fields = ['title', 'description', 'overall_plan']
