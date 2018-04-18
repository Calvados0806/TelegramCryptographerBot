import re

def get_command(message):
	result = re.findall(r'/\w+', message)
	return result