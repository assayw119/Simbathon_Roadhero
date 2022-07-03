from turtle import ondrag
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

category_choice = (
    ('취업','취업'),
    ('창업','창업'),
    ('진학','진학'),
    ('기타','기타'),
)
class Post(models.Model):
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    body = models.TextField()
    category = models.CharField(max_length=10, choices=category_choice, default='취업')
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