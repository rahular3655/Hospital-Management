from django.db import models
from PIL import Image
import os
from io import BytesIO
from django.utils.text import slugify

class BaseImageModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        image_fields = [field.name for field in self._meta.get_fields() if isinstance(field, models.ImageField)]
        for field_name in image_fields:
            image_field = getattr(self, field_name)
            if image_field:
                # Open the original image
                img = Image.open(image_field)

                # Convert image to WebP format
                if img.mode != 'RGB':
                    img = img.convert('RGB')

                # Create a BytesIO buffer to hold the WebP image data
                buffer = BytesIO()

                # Save the image to the buffer in WebP format
                img.save(buffer, format='WEBP')

                # Set the buffer's file pointer to the beginning
                buffer.seek(0)

                # Update the instance with the WebP image
                webp_filename = os.path.splitext(os.path.basename(image_field.name))[0] + '.webp'
                getattr(self, field_name).save(webp_filename, BytesIO(buffer.getvalue()), save=False)

        super().save(*args, **kwargs)


class DropDownClass(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=True)
    is_active = True
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Drop Down'


class DropDown(models.Model):
    value = models.CharField(max_length=100, null=True, blank=True)
    drop_class = models.ForeignKey(DropDownClass, on_delete=models.CASCADE, null=True, blank=True, related_name="dropdowns")

    def __str__(self):
        return self.value