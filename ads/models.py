from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    complete_address = models.CharField(max_length=100)
    photo1_url = models.CharField(max_length=500)
    photo2_url = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def subdescription(self):
        return self.description[:126]
