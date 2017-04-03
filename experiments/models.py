from django.db import models

# Create your models here.


class SimpleEmailMessssage(models.Model):
    subject = models.CharField(max_length=256)
    message = models.CharField(max_length=32767)
    from_addr = models.CharField(max_length=256)
    to_addrs = models.CharField(max_length=1024)

    def __init__(self, subject, message, from_addr, to_addrs):
        self.subject = subject
        self.message = message
        self.from_addr = from_addr
        self.to_addrs = to_addrs

    class Meta:
        managed = False
