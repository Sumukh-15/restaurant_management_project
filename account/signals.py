from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.model import User
from .models import UserProfile

@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@reciever(post_save,sender=User)
def save_create_user(sender, instance, **kwargs):
    instnace.profile.save()


