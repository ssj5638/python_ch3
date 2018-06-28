from django.db import models

# Create your models here.


class Guestbook(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    message = models.CharField(max_length=2000)
    regdate = models.DateTimeField(auto_now=True)      # 자동으로 현재 시간 기록


    def __str__(self):
        return 'Guestbook(%s, %s, %s, %s)' % (self.name, self.password, self.message, str(self.regdate))