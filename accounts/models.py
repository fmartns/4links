from django.db import models
from django.conf import settings
from django.utils.timezone import now

class UserDevice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    device = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=255, blank=True, null=True)
    last_login = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.user.username} - {self.device} - {self.ip_address}" # pylint: disable=no-member
    