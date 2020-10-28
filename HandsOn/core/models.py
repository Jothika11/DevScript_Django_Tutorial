from django.db import models

# Create your models here.
class UserData(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.CharField(max_length=800)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'user_data'