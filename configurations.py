import os

triggers = {
    "more": '>',
    "less": '<',
    "more_eq": '>=',
    "less_eq": '<='
}

binance_url = '''wss://stream.binance.com:9443/stream?streams=
btcusdt@miniTicker/
ethbtc@miniTicker/
dotusdt@miniTicker/
ethusdt@miniTicker'''

token = os.environ.get('access_token')
tg_url = f"https://api.telegram.org/bot{token}/sendMessage?"
chat_id = "@kraud_test_assignment"
