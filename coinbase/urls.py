from django.conf.urls import url
from views import handle_order_callback

urlpatterns = [
    url(r"^cb/$", handle_order_callback, name="coinbase_order_callback")
    ]
