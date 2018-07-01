"module which contains functions for working with messages"
import re

def get_info(message):
	"return dict with message info"
	result = re.search(r'(?P<command>/\w+) (?P<another>(?P<key>\w+) ?(?P<text>.+)?)', message)
	return result
