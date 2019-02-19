from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=256)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    text=models.TextField()
    create_time=models.DateTimeField(default=timezone.now)
    pub_time=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.pub_time=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comment.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("blog:postdetail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title


class comment(models.Model):
    post=models.ForeignKey('blog.post',related_name="comment",on_delete=models.CASCADE)
    author=models.CharField(max_length=256)
    text=models.TextField()
    create_time=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)


    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return reverse('blog:postlist')
    def __str__(self):
        return self.text
