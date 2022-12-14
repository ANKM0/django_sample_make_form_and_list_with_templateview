from django.db import models


class TestData(models.Model):
    number = models.PositiveIntegerField()
    name = models.CharField(max_length=200, blank=False, null=False)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "テストデータ"
