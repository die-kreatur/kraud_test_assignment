import websocket, requests, json, logging
from configurations import triggers, binance_url, tg_url, chat_id


with open('config.json') as file:
    file = file.read()
    config = json.loads(file)


def send_message_to_tg(message):
    """Sends notification to telegram channel"""
    params = {
        'chat_id': chat_id,
        'text': message
        }
    requests.post(tg_url, params=params)


def process_data(currency, price):
    """Checks if retrieved data is corresponding to config.json conditions"""
    trigger = config[currency]['trigger']
    trigger = triggers[trigger]
    price_to_compare = config[currency]['price']
    condition = price + trigger + price_to_compare

    if eval(condition):
        return f"Price has changed.\n{currency} is {price} now."


def on_message(ws, message):
    """Retrieved data processing"""
    data = json.loads(message)['data']
    currency = data['s'][:3] + '/' + data['s'][3:]
    price = data['c']

    notification = process_data(currency, price)
    if notification is not None:
        send_message_to_tg(notification)


def on_close(ws, close_status_code, close_msg):
    """Sends notification to telegram when connection is closed"""
    close_msg = "Connection has been closed, new data cannot be retieved."
    send_message_to_tg(close_msg)


def on_error(ws, error):
    """Logging errors"""
    logging.basicConfig(
        level=logging.ERROR,
        filename='websocket_client.log',
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.error(error)


if __name__ == "__main__":
    ws = websocket.WebSocketApp(binance_url,
        on_message=on_message,
        on_close=on_close,
        on_error=on_error
    )
    ws.run_forever()
