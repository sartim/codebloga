from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    code = models.TextField()
    pub_date = models.DateTimeField()
    likes = models.IntegerField()
    image = models.FileField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})
