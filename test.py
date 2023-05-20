import sender_request
import data

#сохранение трека заказа
def save_track():
    response = sender_request.post_new_orders()
    return response.json().get('track')

#проверка кода 200
def test_track():
    track = save_track()
    response = sender_request.get_order_by_track(track)
    assert response.status_code == 200