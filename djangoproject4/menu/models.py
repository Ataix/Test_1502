from django.db import models
from django.urls import reverse


class MenuCategory(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=255, blank=True, null=False)
    category = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE, blank=False, null=False
    )
    path = models.CharField(max_length=1000, blank=True, null=False)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_DEFAULT, null=True, blank=True, default=0
    )

    def __str__(self):
        return self.name
