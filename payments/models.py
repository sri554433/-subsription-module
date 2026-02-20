from django.db import models
from django.contrib.auth.models import User


# SUBSCRIPTION MODEL
# stores selected plan and price
class Subscription(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    plan_name = models.CharField(max_length=50)

    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.user.email} - {self.plan_name}"



# PAYMENT MODEL
# stores payment details
class Payment(models.Model):

    PAYMENT_METHODS = (
        ("upi", "UPI"),
        ("card", "Card"),
        ("qr", "QR"),
    )

    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    plan = models.CharField(max_length=50)

    amount = models.IntegerField()

    method = models.CharField(max_length=20, choices=PAYMENT_METHODS)

    transaction_id = models.CharField(max_length=200, blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return f"{self.user.email} - {self.plan} - {self.status}"
