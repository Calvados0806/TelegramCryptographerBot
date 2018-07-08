"module which contains functions for working with messages"
import re

def get_info(message):
	"returns dict with message info"
	command = get_command(message)
	key = get_key(message)
	text = get_text(message)
	if command and key and text:
		return {"command": command, "key": key, "text": text}
	else:
		return None

def get_command(message):
	"returns command from message"
	result = re.findall(r'/\w+', message)
	if result:
		return result[0]
	return None

def get_key(message):
	"returns key from message"
	result = re.findall(r'/\w+ ([\w\d]+)', message)
	if result:
		return result[0]
	return None

def get_text(message):
	"returns text from message"
	result = re.findall(r'/\w+ [\w\d]+ (.+)', message)
	if result:
		return result[0]
	return None