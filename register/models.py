from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modification = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Users(BaseModel):
    name = models.CharField(max_length=255,
                            null=False)
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)