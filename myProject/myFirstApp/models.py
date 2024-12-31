from django.db import models

class users_db(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.first_name

