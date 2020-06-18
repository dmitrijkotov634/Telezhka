from requests import Session

class ApiError(Exception):
	pass

class Telegram:
	def __init__(self, token):
		self.session = Session()
		self.api = "https://api.telegram.org/bot%s/" % (token)

	def method(self, name="getMe", data={}):
		response = self.session.get(self.api+name, data=data).json()
		if response["ok"]:
			return response["result"]
		else:
			raise ApiError("[{}] {}".format(response["error_code"], response["description"]))
	
	def listen(self, timeout=25):
		ts = 0
		response = self.getUpdates(timeout=timeout, offset=-1)
		if response:
			ts = response[0]["update_id"] + 1
		while True:
			response = self.getUpdates(offset=ts, timeout=timeout)
			if response:
				for event in response:
					yield event["message"]
					ts += 1

	def __getattr__(self, attr):
		return lambda **data: self.method(attr, data)