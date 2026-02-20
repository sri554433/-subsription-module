from django.contrib import admin
from .models import Payment, Subscription


# PAYMENT ADMIN PANEL
class PaymentAdmin(admin.ModelAdmin):

    list_display = (

        "id",
        "user",
        "plan",
        "amount",
        "method",
        "transaction_id",
        "status",
        "created_at"

    )

    list_filter = (

        "status",
        "method",
        "plan"

    )

    search_fields = (

        "user__username",
        "transaction_id"

    )

    ordering = ("-created_at",)



# SUBSCRIPTION ADMIN PANEL
class SubscriptionAdmin(admin.ModelAdmin):

    list_display = (

        "id",
        "user",
        "plan_name",
        "price",
        "created_at"

    )

    search_fields = (

        "user__username",
        "plan_name"

    )

    ordering = ("-created_at",)



# REGISTER MODELS
admin.site.register(Payment, PaymentAdmin)

admin.site.register(Subscription, SubscriptionAdmin)

