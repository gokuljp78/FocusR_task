from django.db import models
# import uuid


class user(models.Model):
    # id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=40,null=True)
    ac_number=models.IntegerField()
    mobile=models.IntegerField()


class bank_detials(models.Model):
    bal=models.FloatField()

# Create your models here.
