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
	if "text" in event:
		if event["text"] == "/hello":
			api.sendMessage(text="Hello", chat_id=event["chat"]["id"])
```

