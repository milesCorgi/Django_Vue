from django.db import models
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    Todo_body = models.TextField(max_length=140)
    add_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, default="todo")  # ready running error finish

    def __unicode__(self):
        return self.Todo_body

    class Meta:
        ordering = ("-add_time",)
        #排列顺序按这个定的
        index_together = (('id', 'add_time'),)
        #说是为了提高性能建立的索引