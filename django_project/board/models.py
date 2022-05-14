from django.db import models
from django.conf import settings

class Board(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

class Card(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True)
    progress = models.CharField(max_length=30, choices=[('onHold', 'onHold'), ('inProgress', 'inProgress'), ('needsReview', 'needsReview'), ('approved', 'approved')])
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
