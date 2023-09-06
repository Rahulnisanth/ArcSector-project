
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete


class Profile(models.Model):
    user = models.OneToOneField(
        User, to_field="id", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    skills = models.ManyToManyField('Skills', blank=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    occupation = models.CharField(max_length=200, blank=True, null=True)
    DOB = models.DateField(null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    experience = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    profile_pic = models.ImageField(
        default='default__profile.png', upload_to='profile_pics', )
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_facebook = models.CharField(max_length=200, null=True, blank=True)
    social_twitter = models.CharField(max_length=200, null=True, blank=True)
    social_instagram = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          editable=False, primary_key=True)

    def __str__(self) -> str:
        return str(self.user)


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            name=user.username,
            email=user.email,
        )


post_save.connect(createProfile, sender=User)


class Skills(models.Model):
    # rater = models.ForeignKey(
    #     Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    # created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)
