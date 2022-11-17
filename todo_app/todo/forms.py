from django import forms
from . models import Todo
from django.core.validators import validate_image_file_extension


class TodoForm(forms.ModelForm):
    IS_FINISHED = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    task = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', "rows": 3, "cols": 10}), required=False)

    todo_image = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'form-control', 'accept': 'image/*'}), validators=[validate_image_file_extension], required=False)
    status = forms.CharField(
        max_length=1,
        widget=forms.Select(choices=IS_FINISHED, attrs={
            'class': 'form-select'}),
    )

    class Meta:
        model = Todo
        exclude = ('created_at', 'update_at', )
