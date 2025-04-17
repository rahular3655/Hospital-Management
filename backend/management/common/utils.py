import os
from uuid import uuid4

from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput


def random_file_name(instance, filename):
    parts = filename.split("/")
    name, ext = os.path.splitext(parts.pop())
    parts.append(f"{uuid4()}{ext}")
    return "/".join(parts)


class CustomizedFormFieldMixin(admin.ModelAdmin):
    """
    A mixin class to customize form fields size in Django admin.
    """

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 140})},
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.formfield_overrides.update(kwargs.get('formfield_overrides', {}))