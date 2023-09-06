
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import *




def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteProfile(sender, instance, **kwargs):
    user = instance.user
    user.delete()



post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deleteProfile, sender=Profile)
