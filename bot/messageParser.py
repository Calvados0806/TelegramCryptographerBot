"module which contains functions for working with messages"
import re

def get_command(message):
	"return list of commands founded in message"
	result = re.findall(r'/\w+', message)
	return result
