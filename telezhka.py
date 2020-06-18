from requests import Session

class ApiError(Exception):
	pass

class telegram:
	def __init__(self, token):
		self.session = Session()
		self.api = "https://api.telegram.org/bot{}/".format(token)

	def method(self, name="getMe", data={}):
		response = self.session.get(self.api+name, data=data).json()
		if response["ok"]:
			return response["result"]
		else:
			raise ApiError("[{}] {}".format(response["error_code"], response["description"]))
	
	def listen(self, timeout=25, limit=10):
		ts = 0
		while True:
			response = self.getUpdates(offset=ts, timeout=timeout, limit=limit)
			if response:
				ts = response[-1]["update_id"]
				for event in response:
					yield event["message"]
				ts += 1

	def __getattr__(self, attr):
		return lambda **data: self.method(attr, data)