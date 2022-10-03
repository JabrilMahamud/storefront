from django.db import models

# Create your models here.
class Metadata(models.Model):
    account_name = models.CharField(max_length=400)
    account_no=models.CharField(max_length=400)
    account_status=models.CharField(max_length=400)

    def __str__(self):
        return self.account_name