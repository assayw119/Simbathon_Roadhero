from asyncore import write
from calendar import prmonth
from turtle import ondrag
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

post_choice = (
    ('취업','취업'),
    ('창업','창업'),
    ('진학','진학'),
    ('기타','기타'),
)

write_choice = (
    ('질문','질문'),
    ('정보','정보'),
    ('생활','생활'),
    ('기타','기타'),
)
class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    view_users = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=post_choice, default='취업')
    image = models.ImageField(upload_to='post/', blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:20]

class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post ,on_delete=models.CASCADE, related_name ='comments')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)

class Community(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    category = models.CharField(max_length=10, choices=write_choice, default='질문')

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.body) >= 100:
            return self.body[:100]
        else:
            return self.body[:100]
    