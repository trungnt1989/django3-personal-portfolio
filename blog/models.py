from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    # dong nay duoc them vao de hien thi noi dung tung title trong trang admin cua app
    def __str__(self):
        return self.title