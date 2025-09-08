from django.db import models

# Create your models here.
class Feedback(models.Model):
    comment = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add =True)

    def __str__(self):
        return f"Feedback #{self.id} at {self.submitted_at}"