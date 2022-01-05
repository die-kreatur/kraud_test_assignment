# Client for Binance Websocket API
Client for <a href="https://www.binance.com/en" target="_blank">Binance</a> Websocket API with sending notifications to <a href="https://t.me/kraud_test_assignment" target="_blank">telegram channel</a>.

## Technologies
- Python 3.9
- Python3 built-in modules **logging** and **json**
- websocket-client 1.2.3
- requests 2.27.0

All the dependencies may be found in **requirements.txt**.

## Functionality
- When the script **websocket_client.py** is run, connection with Binance API is established.
- Retrieved data is parsed by **on_message** function and compared to **config.json** conditions.
- If the retrieved data is corresponding to **config.json** conditions, new notification will be sent to telegram channel.
- If any exception occurres, it will be written to **websocket_client.log** file.
- If connection is dead, a notification will be sent to telegram channel.
