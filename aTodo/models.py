from django.db import models

# Create your models here.
class Todo(models.Model):
    Todo_name = models.TextField(max_length=140)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.Todo_name