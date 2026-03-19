from django.db import models

class ScrapedContent(models.Model):
    source = models.CharField(max_length=50, db_index=True)
    category = models.CharField(max_length=100, db_index=True)
    external_id = models.CharField(max_length=100, unique=True)
    title = models.TextField()
    url = models.URLField(max_length=500)
    author = models.CharField(max_length=100)
    created_at_external = models.DateTimeField()
    raw_data = models.JSONField(default=dict) 

    class Meta:
        indexes = [models.Index(fields=['source', 'category'])]
