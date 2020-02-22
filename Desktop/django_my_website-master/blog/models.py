from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    description = models.TextField(blank=False)


class Post(models.Model):
    title = models.CharField(max_length=30)  #블로그에서 제목을 의미
    content = models.TextField()  #글에 들어갈 내용

    head_image = models.ImageField(upload_to='blog/%y/%m/%d/', blank=True)

    created = models.DateTimeField()  #언제 작성이 되었는지, 어떤 사용자가 사용했는지
    author = models.ForeignKey(User, on_delete=True)

    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{} :: {}'.format(self.title, self.author)

    def get_absolute_url(self):
        return '/blog/{}/'.format(self.pk)


