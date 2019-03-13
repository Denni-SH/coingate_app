import os
from coingate.client import CoinGateV2Client, CoinGateV2Order

CLIENT = CoinGateV2Client(os.getenv("APP_ID"), os.getenv("API_KEY"))
DEFAULT_CURRENCY = "USD"


def place_order(pay_amount, order_url):

    orders = list(CLIENT.iterate_all_orders())
    order_id = int(orders[0].order_id) + 1 if orders else 1
    new_order = CoinGateV2Order.new(
        order_id,
        pay_amount,
        DEFAULT_CURRENCY,
        DEFAULT_CURRENCY,
        callback_url=order_url,
        cancel_url=order_url,
        success_url=order_url,
    )

    return CLIENT.create_order(new_order)


def process_client_order_list():

    raw_order_list = list(CLIENT.iterate_all_orders())
    processed_order_list = list()
    for order in raw_order_list:
        temp_order = order.to_request_data()
        temp_order["status"] = order.status
        temp_order["created_at"] = order.created_at
        processed_order_list.append(temp_order)

    return processed_order_list
