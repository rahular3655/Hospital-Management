from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django_lifecycle import hook, LifecycleModelMixin, AFTER_CREATE, AFTER_UPDATE, BEFORE_CREATE, BEFORE_UPDATE
from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail.fields import ImageField
from sorl.thumbnail import get_thumbnail
from django.utils.text import slugify
from common.models import DropDown,BaseImageModel
from common.utils import random_file_name


class StatusChoices(models.TextChoices):
    open = ('open', 'open')
    in_progress = ('in_progress', 'in progress')
    resolved = ('resolved', 'resolved')
    
    
class User(LifecycleModelMixin, AbstractUser):
    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    change_email = models.EmailField(null=True, blank=True)
    contact_number = PhoneNumberField(null=True, blank=True, unique=True)
    change_contact_number = PhoneNumberField(null=True, blank=True, unique=True)
    is_deleted = models.BooleanField(default=False)
    is_username_updated = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=True)
    objects = UserManager()

    # user_objects = UserQuerySet.as_manager()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    @hook(BEFORE_CREATE, when='is_superuser', is_not=False)
    def set_superuser_active(self):
        self.is_active = True

    @hook(AFTER_CREATE, when_any=['is_superuser', 'is_staff'], is_now=False, priority=2)
    def create_profile(self):
        UserProfile.objects.create(user=self)

    @hook(BEFORE_UPDATE, when='username', has_changed=True, is_not=None)
    def update_is_username_updated(self):
        self.is_username_updated = True
        
    @hook(BEFORE_UPDATE, when='contact_number', has_changed=True, is_not=None)
    def update_is_contact_number_verified(self):
        self.is_contact_number_verified = True


class UserProfile(LifecycleModelMixin, BaseImageModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        help_text="One user is relate only with one profile."
    )

    gender = models.ForeignKey(DropDown, on_delete=models.CASCADE, blank=True, null=True, related_name="gender",
                               limit_choices_to={'drop_class__slug': 'gender'})
    profile_image = ImageField(upload_to=random_file_name, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    pass

    @property
    def thumbnail(self):
        if self.profile_image:
            return get_thumbnail(self.profile_image, '200x20', quality=90)
        return None
    
        
class SupportRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="support",
                             help_text="One user can have multiple support requests."
                             )
    title = models.TextField()
    message = models.TextField()
    status = models.CharField(max_length=100, choices=StatusChoices.choices, default=StatusChoices.open)
    comments = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email
    
    
    