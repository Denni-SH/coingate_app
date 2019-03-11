import os

from coingate.client import CoinGateV2Client, CoinGateV2Order
from django.shortcuts import render, redirect

CLIENT = CoinGateV2Client(os.getenv("APP_ID"), os.getenv("API_KEY"))
DEFAULT_CURRENCY = "USD"
ORDER_LIST_URL = "http://127.0.0.1:8000/order_list"


def index(request):
    content = dict()
    content['title'] = "CoinIntegro"
    return render(request, "index.html", content)


def create_order(request):
    rate_amount = request.POST.get("order_amount")
    orders = list(CLIENT.iterate_all_orders())
    order_id = int(orders[0].order_id) + 1 if orders else 1
    order_url = ORDER_LIST_URL
    new_order = CoinGateV2Order.new(
        order_id,
        rate_amount,
        DEFAULT_CURRENCY,
        DEFAULT_CURRENCY,
        callback_url=order_url,
        cancel_url=order_url,
        success_url=order_url,
    )

    placed_order = CLIENT.create_order(new_order)
    payment_url = placed_order.payment_url if placed_order else '/'

    return redirect(payment_url)


def get_orders_list(request):
    raw_order_list = list(CLIENT.iterate_all_orders())
    proccessed_order_list = []
    for order in raw_order_list:
        temp_order = order.to_request_data()
        temp_order["status"] = order.status
        temp_order["created_at"] = order.created_at
        proccessed_order_list.append(temp_order)
    
    content = dict()
    content['title'] = "Order list"
    content["orders"] = proccessed_order_list
    return render(request, "order_list.html", content)
