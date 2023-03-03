from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=400, null=True, blank=True)
    source_link = models.CharField(max_length=400, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    vote_count = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    tag = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    VOTE_TYPE = (
        ("+", "Ijobiy"),
        ("-", "Salbiy")
    )
    body = models.TextField(default=' ')
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name