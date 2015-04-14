import re


def search(patter, text):
	"Return True if pattern appears anywhere in text."
	if pattern.startwith('^'):
		return match(pattern[1:], text)
	else:
		return match('.*' + pattern, text)

def match(pattern, text):
	"Return True if pattern appears at the start of text."
	if pattern[0] == '':
		return True
	elif pattern[0] == '$':
		return pattern[1:] == text[0:len(pattern)-1]
	elif len(pattern) > 1 and pattern[1] in '*?':
		if pattern[1] == '*':
			for index in range(len(text)):
				if text[index] != pattern[0]:
					return match(pattern[2:], text[index:])
			return True
		else:
			if text[0] == pattern[0]:
				return match(pattern[2:], text[1:])
			else:
				return match(pattern[2:], text)
	else:
		return (match1(pattern[0], text) and
				match(pattern[1:], text[1:]))

def match1(p, text):
	"""Return True if first character of text matched
	pattern character p."""
	if not text:
		return False
	return p == '.' or p == text[0]

def match_star(p, pattern, text):
	"""Return True if any number of char p,
	followed by pattern, matched text."""
	return (match(pattern, text)) or
			(match1(p, text) and
			 match_star(p, pattern, text[1:]))
