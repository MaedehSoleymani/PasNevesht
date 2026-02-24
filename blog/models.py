#pasnevesht models

from django.db import models

class Post(models.Model):
    title= models.CharField(max_length=200)
    content=models.TextField()
    #author=
    created_date=models.DateTimeField(auto_now_add=True)
    publish_date=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='blog/', default='blog/default.webp')
    views=models.IntegerField(null=False, default=0)
    comments=models.TextField()
    #tags=
    status=models.BooleanField(null=False)

    def __str__(self):
        return "{} - {}".format(self.id, self.title)