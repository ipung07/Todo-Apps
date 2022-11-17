from django.db import models
from django.core.validators import validate_image_file_extension
from django.forms import ModelForm

# Create your models here.


class Todo(models.Model):
    IS_FINISHED = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    task = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=IS_FINISHED)
    todo_image = models.ImageField(
        default="default.jpg", null=True, upload_to='img/todo/', validators=[validate_image_file_extension], blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
