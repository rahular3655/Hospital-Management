from django.db import models
from accounts.models import User
from django.utils.text import slugify
from treebeard.mp_tree import MP_Node

# Create your models here.
     
class LeaveApplicationChoices(models.TextChoices):
    waiting = ('waiting','Waiting')
    approved  = ('approved','Approved')
    rejected =  ('rejected','Rejected')
 
    
class StaffCategory(MP_Node):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name="categories")
    name = models.CharField(blank=False,max_length=100,null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=False, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    node_order_by = ['name']
    
    def activate_descendants(self):
        """
        Activate all descendants of this category.
        """
        descendants = self.get_descendants()
        for descendant in descendants:
            descendant.is_active = True
            descendant.save()

    def deactivate_descendants(self):
        """
        Deactivate all descendants of this category.
        """
        descendants = self.get_descendants()
        for descendant in descendants:
            descendant.is_active = False
            descendant.save()

    def save(self, *args, **kwargs):
        if not self.is_active:  # Check if the category is being deactivated
            self.deactivate_descendants()  # Deactivate all descendants
        elif self.is_active:  # Check if the category is being activated
            self.activate_descendants()  # Activate all descendants
        super(StaffCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Staff Categories"

    def __str__(self):
        level_indicator = '→' * self.depth  # Use arrows (→) for indentation
        return '%s %s' % (level_indicator, self.name)
    
    
class LeaveApplication(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="leave_application")
    subject = models.TextField(blank=True)
    date_of_leave = models.DateField(blank=False)
    is_medical_leave = models.BooleanField(default=False)
    is_emergency = models.BooleanField(default=True)
    is_approved = models.CharField(default="Waiting",choices=LeaveApplicationChoices.choices)
    
    