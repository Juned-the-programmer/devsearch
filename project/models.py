from django.db import models
import uuid
from pages.models import Profile

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile , on_delete=models.SET_NULL , null=True,blank = True)
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to="project_images", null=True, blank=True , default="default.jpg")
    description = models.TextField(null=True , blank=True)
    demo_link = models.CharField(max_length=2000,null=True, blank=True)
    source_link = models.CharField(max_length=2000,null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0,null=True, blank=True)
    vote_ratio = models.IntegerField(default=0,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True , primary_key=True , editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio' , '-vote_total' , 'title']

    @property
    def reviewrs(self):
        queryset = self.review.set_all().values_list('owner__id' , flat=True)
        return quesryset


class Review(models.Model):
    VOTE_TYPES = (
        ('up' , 'Up Vote'),
        ('down' , 'Down Vote')
    )
    owner = models.ForeignKey(Profile , on_delete=models.CASCADE , null=True , blank=True) 
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body  = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPES)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True ,primary_key=True ,editable=False)

    class Meta:
        unique_together = [
            ['owner' , 'project']
        ]

    def __str__(self):
        return self.value

    @property
    def getVoteCount(self):
        reviews = self.reviews_set.all()
        upvotes = reviews.filter(value='up')
        totalvotes = reviews.count()

        ratio = (upvotes / totalvotes) * 100

        self.vote_total = totalvotes
        self.vote_ratio = ratio
        self.save()

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True ,primary_key=True ,editable=False)

    def __str__(self):
        return self.name


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']
    