# Telezhka
![pypi](https://badge.fury.io/py/Telezhka.svg)

Telegram api library in python

*Installation*:

`pip install --upgrade Telezhka`

*Simple bot*:
```python
from Telezhka import *
api = Telegram("883304628:ONTB4H2SAMPLEtext9m0g")

for event in api.listen():
	if "message" in event and "text" in event["message"]:
		if event["message"]["text"] == "/hello":
			api.sendMessage(text="Hello", chat_id=event["message"]["chat"]["id"])
```

