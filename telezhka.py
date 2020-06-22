from requests import Session
import json

class ApiError(Exception):
	pass
	
class Keyboard:
	def __init__(self, mode="keyboard", **args):
		self.mode = mode
		self.keyboard = {mode:[[]]}
		self.keyboard.update(args)
		
	def add_line(self, *args):
		self.keyboard[self.mode].append(list(args))
	
	def add_button(self, **args):
		self.keyboard[self.mode][-1].append(args)
	
	def clear(self):
		self.keyboard[self.mode] = [[]]
		
	def compile(self):
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
	
	def listen(self, timeout=25):
		ts = 0
		response = self.getUpdates(offset=-1)
		if response:
			ts = response[0]["update_id"] + 1
		while True:
			response = self.getUpdates(offset=ts, timeout=timeout)
			if response:
				for event in response:
					yield event
					ts = event["update_id"] + 1

	def __getattr__(self, attr):
		return lambda **data: self.method(attr, data)