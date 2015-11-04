from django.db import models


class User(models.Model):
    ACTIVE = "active"
    INACTIVE = "inactive"
    STATUS_TYPE = (
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive")
    )

    name = models.CharField(max_length=64)
    slack_name = models.CharField(max_length=32, blank=True)
    status = models.CharField(choices=STATUS_TYPE, default=ACTIVE, max_length=16)
    icon_url = models.TextField(blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_users(cls, status=ACTIVE):
        users = cls.objects.all()
        if status:
            users = users.filter(status=status)
        return users
