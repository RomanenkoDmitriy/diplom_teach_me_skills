from django.db import models
from django.contrib.auth import get_user_model
# from django.urls import reverse



class AddDateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CompletedWork(AddDateTimeMixin):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    overall_plan = models.ImageField(upload_to='images/')

    # def get_absolute_url(self):
    #     return reverse('detail', kwargs={'pk': self.pk})

    # @property
    # def overall_plan_url(self):
    #     if self.overall_plan and hasattr(self.overall_plan, 'url'):
    #         return self.overall_plan.url

    def __str__(self):
        return self.title


class FotoWork(AddDateTimeMixin):
    file = models.FileField(upload_to='images/')
    completed_work = models.ForeignKey('CompletedWork', on_delete=models.CASCADE)


class CommentsWork(AddDateTimeMixin):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField()
    completed_work = models.ForeignKey('CompletedWork', on_delete=models.CASCADE)
