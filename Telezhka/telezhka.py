from requests import Session
import json

class ApiError(Exception):
    pass
    
class Update(dict):
	def __getattr__(self, attr):
		if isinstance(self[attr], dict):
			return Update(self[attr])
		else:
			return self[attr]
			
class Keyboard:
    def __init__(self, mode="keyboard", **args):
        self.mode = mode
        self.keyboard = {mode: [[]]}
        self.keyboard.update(args)

    def add_line(self, *args):
        """
        Adds a new line in the keyboard.
        """
        self.keyboard[self.mode].append(list(args))

    def add_button(self, **args):
        """
        Adds a new button in the keyboard.
        """
        self.keyboard[self.mode][-1].append(args)

    def clear(self):
        """
        Remove all buttons on the keyboard.
        """
        self.keyboard[self.mode] = [[]]

    def compile(self):
        """
        Converts the keyboard to JSON for subsequent sending in the message.
        """
        return json.dumps(self.keyboard)

class Telegram:
    def __init__(self, token):
        self.session = Session()
        self.api = "https://api.telegram.org/bot" + token + "/"

    def method(self, name="getMe", data={}):
        response = self.session.get(self.api+name, data=data).json()
        if response["ok"]:
            return response["result"]
        else:
            raise ApiError("[%s] %s" % (response["error_code"], response["description"]))

    def listen(self, timeout=27):
        ts = 0
        response = self.method("getUpdates", {"offset": -1})
        if response:
            ts = response[0]["update_id"] + 1
        while True:
            response = self.method("getUpdates", {"offset": ts, "timeout": timeout})
            if response:
                for event in response:
                    yield Update(event)
                    ts = event["update_id"] + 1

    def __getattr__(self, attr):
        return lambda **data: self.method(attr, data)
    
    def __repr__(self):
        return f"Bot api <{self.method('getMe')['username']}>"
        
    def reply(self, update, **args):
        if "message" in update:
            params = {"chat_id": update["message"]["chat"]["id"], "reply_to_message_id": update["message"]["message_id"]}
            params.update(args)
            self.method("sendMessage", params)