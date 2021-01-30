from django.db import models


class PageView(models.Model):
    url = models.CharField(max_length=70, blank=True, null=True, unique=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.url} - {self.views}'
