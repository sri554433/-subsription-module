from django.contrib import admin
from django.urls import path
from payments import views as pay_views


urlpatterns = [

    # ADMIN PANEL
    path('admin/', admin.site.urls),


    # AUTHENTICATION
    path('', pay_views.login_page, name="login"),

    path('register/', pay_views.register_page, name="register"),

    path('logout/', pay_views.logout_page, name="logout"),


    # PLANS
    path('plans/', pay_views.plans_page, name="plans"),


    # PAYMENT
    path('payment/', pay_views.payment_page, name="payment"),


    # PROCESSING PAGE
    path(
        'processing/<int:payment_id>/',
        pay_views.processing_page,
        name="processing"
    ),


    # SUCCESS PAGE
    path('success/', pay_views.success_page, name="success"),


    # API ROUTES
    path(
        'api/create-payment/',
        pay_views.create_payment,
        name="create_payment"
    ),

    path(
        'api/check-payment/<int:payment_id>/',
        pay_views.check_payment,
        name="check_payment"
    ),

]
