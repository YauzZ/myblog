from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.CharField(max_length=35)
    email = models.EmailField()
    homepage = models.URLField()
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=20)

    def __str__(self):
        return 'Name: %s Email: %s HomePage: %s\n'\
                'Time: %s IP: %s \n'\
                'Title: %s\nContent: %s\n'\
                % (self.name,self.email,self.homepage,
                        self.time,self.ip,self.title,
                        self.content);

