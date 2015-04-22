from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """tag data model"""
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta(object):
        """meta information for tag class"""
        ordering = ('name',)


class BlogPost(models.Model):
    """blog post data model"""
    topic = models.CharField(max_length=255)
    content = models.TextField()
    published = models.DateTimeField()
    author = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.topic

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blog.views.detail', args=[str(self.id)])

    class Meta(object):
        """meta information for blog post class"""
        ordering = ('published',)


