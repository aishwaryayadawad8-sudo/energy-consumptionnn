from django.db import models
from django.utils import timezone


class EmailLog(models.Model):
    """Track all email alerts sent to countries"""
    
    STATUS_CHOICES = [
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('pending', 'Pending'),
    ]
    
    ALERT_TYPE_CHOICES = [
        ('critical', 'Critical'),
        ('needs_improvement', 'Needs Improvement'),
        ('good', 'Good'),
        ('excellent', 'Excellent'),
    ]
    
    country = models.CharField(max_length=100)
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    alert_type = models.CharField(max_length=50, choices=ALERT_TYPE_CHOICES)
    electricity_access = models.FloatField()
    year = models.IntegerField()
    sent_at = models.DateTimeField(default=timezone.now)
    error_message = models.TextField(blank=True, null=True)
    sent_by = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        ordering = ['-sent_at']
        verbose_name = 'Email Log'
        verbose_name_plural = 'Email Logs'
    
    def __str__(self):
        return f"{self.country} - {self.status} - {self.sent_at.strftime('%Y-%m-%d %H:%M')}"
