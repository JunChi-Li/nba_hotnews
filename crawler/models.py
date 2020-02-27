from django.db import models

# Create your models here.
class nba_news(models.Model):
    nba_title = models.CharField(max_length = 30, blank=True, default='')
    nba_content = models.TextField(blank=True, default='')
    nba_url = models.TextField(blank=True, default='')
    nba_time = models.CharField(max_length=50, null=True, default='')
