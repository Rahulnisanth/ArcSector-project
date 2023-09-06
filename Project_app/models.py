from django.db import models
from user.models import Profile
import uuid
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    project_image = models.ImageField(
        null=True, blank=True, upload_to="project_images/")
    source_link = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    type_design = models.CharField(max_length=200)
    start_date = models.DateField()
    completed_date = models.DateField()
    voucher = models.IntegerField(default=0, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL),

    def __str__(self) -> str:
        return str(self.title)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)


class Reviews(models.Model):
    vote_type = (
        ('up', 'up vote'),
        ('down', 'dowm vote'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self)
