from django.db import models

class Feedback(models.Model):
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    rating = models.IntegerField(null=True, blank=True)  # Ex.: nota de 1 a 5
    date_submitted = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'feedback'

    def __str__(self):
        return f"Feedback de {self.user_name} - {self.date_submitted}"

