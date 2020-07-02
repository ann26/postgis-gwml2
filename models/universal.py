from django.contrib.gis.db import models


class Quantity(models.Model):
    """ Model to define quantity. """
    value = models.FloatField(
        null=True, blank=True)
    unit = models.CharField(
        max_length=256,
        null=True, blank=True)

    def __str__(self):
        return '{} ({})'.format(self.value, self.unit)


class GWTerm(models.Model):
    """ Abstract model for Term """
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True