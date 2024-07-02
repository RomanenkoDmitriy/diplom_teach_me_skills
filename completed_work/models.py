from django.db import models
from django.contrib.auth import get_user_model


class AddDateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CompletedWork(AddDateTimeMixin):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    overall_plan = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class FotoWork(AddDateTimeMixin):
    file = models.ImageField(upload_to='images/')
    completed_work = models.ForeignKey('CompletedWork', on_delete=models.CASCADE, related_name='foto')


class CommentsWork(AddDateTimeMixin):
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(max_length=500)
    completed_work = models.ForeignKey('CompletedWork', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-created_at']
