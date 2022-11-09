from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Todo(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('todo-home', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
