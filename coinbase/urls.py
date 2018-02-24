from django.conf.urls import url


urlpatterns = [
    url(r"^cb/$", "handle_order_callback", name="coinbase_order_callback")
    ]
