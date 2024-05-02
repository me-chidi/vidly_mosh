from typing import Any
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from datetime import timedelta
# Create your models here.

class Checkout(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    payment_status = models.CharField(
            max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    date_created = models.DateTimeField(default=timezone.now)
    duration = models.PositiveSmallIntegerField(default=None, null=True) 
    
    @classmethod
    def _duration(cls, self):
        self.end = timedelta(days=1) + self.date_created
        if self.duration:
            cls.date_end = models.DateTimeField(default=self.end, null=True)

    def __str__(self):
        return str(self.id)


class CheckoutItem(models.Model):
    checkout = models.ForeignKey(Checkout, on_delete=models.PROTECT)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.PROTECT)
    content_object = GenericForeignKey()
        










    # # TL; since datetimefield is not a variable in normal terms 
    # # calling these functions save a value to it
    # def clean(self):
    #     if not self.date_end:
    # self.date_end = self.date_created + timedelta(days=1)

    # def save(self, **kwargs):
    #     self.clean
    #     return super().save(**kwargs)


