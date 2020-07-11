<div align="center">
	<h1>Telezhka</h1>

Telegram api library in python

![pypi](https://badge.fury.io/py/Telezhka.svg)

</div>

## Install
`pip install --upgrade Telezhka`

## Simple usage
```python
from Telezhka import Telegram
api = Telegram("883304628:ONTB4H2SAMPLEtext9m0g")

for event in api.listen():
    if "message" in event and "text" in event.message:
        if event.message.text == "/hello":
            api.sendMessage(text="Hello :)", chat_id=event.message.chat.id)
```

## Keyboard usage
```python
from Telezhka import Keyboard

kb = Keyboard(resize_keyboard=True)
kb.add_button(text="hello")
kb.add_line({"text": "hello2"})
# Send message with keyboard
api.sendMessage(reply_markup=kb.compile(), text="Hello", chat_id=event.message.chat.id)
```

