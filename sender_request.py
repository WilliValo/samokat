import configuration
import requests
import data

# создание заказа
def post_new_orders(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=order_body)


#получение заказа по треку
def get_order_by_track(track):
    params = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDERS_TRACK, params=params)
