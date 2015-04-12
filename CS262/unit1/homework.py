import re


# Title: Summing Numbers

# Write a procedure called sumnums(). Your procedure must accept as input a
# single string. Your procedure must output an integer equal to the sum of
# all integer numbers (one or more digits in sequence) within that string.
# If there are no decimal numbers in the input string, your procedure must
# return the integer 0. The input string will not contain any negative integers.
#
# Example Input: "hello 2 all of you 44"
# Example Output: 46
#
# Hint: int("44") == 44


def sumnums(sentence): 
	numbers = [int(num) for num in re.findall(r"[0-9]+", sentence)]
	return sum(numbers)

# This problem includes an example test case to help you tell if you are on
# the right track. You may want to make your own additional tests as well.

test_case_input = """The Act of Independence of Lithuania was signed 
on February 16, 1918, by 20 council members."""

test_case_output = 1954

if sumnums(test_case_input) == test_case_output:
  print ("Test case passed.")
else:
  print ("Test case failed:")
  print (sumnums(test_case_input))


# ---------------------------------------------------------------------------
#
# Singly-Hyphenated Words

# We examined hyphenated words in a quiz in class. In this problem you
# will get a chance to handle them correctly. 
# 
# Assign to the variable regexp a Python regular expression that matches 
# both words (with letters a-z) and also singly-hyphenated words. If you 
# use grouping, you must use (?: and ) as your regular expression
# parentheses. 
#
# Examples: 
#
# regexp exactly matches "astronomy"  
# regexp exactly matches "near-infrared"  
# regexp exactly matches "x-ray"  
# regexp does not exactly match "-tricky" 
# regexp does not exactly match "tricky-" 
# regexp does not exactly match "large - scale" 
# regexp does not exactly match "gamma-ray-burst" 
# regexp does not exactly match "" 

# Your regular expression only needs to handle lowercase strings.

# In Python regular expressions, r"A|B" checks A first and then B - it 
# does not follow the maximal munch rule. Thus, you may want to check 
# for doubly-hyphenated words first and then non-hyphenated words.

regexp = r"(?:[a-z]+-[a-z]+)|[a-z]+" # you should replace this with your regular expression

# This problem includes an example test case to help you tell if you are on
# the right track. You may want to make your own additional tests as well.

test_case_input = """the wide-field infrared survey explorer is a nasa
infrared-wavelength space telescope in an earth-orbiting satellite which
performed an all-sky astronomical survey. be careful of -tricky tricky-
hyphens --- be precise."""

test_case_output = ['the', 'wide-field', 'infrared', 'survey', 'explorer',
'is', 'a', 'nasa', 'infrared-wavelength', 'space', 'telescope', 'in', 'an',
'earth-orbiting', 'satellite', 'which', 'performed', 'an', 'all-sky',
'astronomical', 'survey', 'be', 'careful', 'of', 'tricky', 'tricky',
'hyphens', 'be', 'precise']

if re.findall(regexp, test_case_input) == test_case_output:
  print ("Test case passed.")
else:
  print ("Test case failed:") 
  print (re.findall(regexp, test_case_input))


# --------------------------------------------------------------------------
#
# Title: Simulating Non-Determinism

# Each regular expression can be converted to an equivalent finite state
# machine. This is how regular expressions are implemented in practice. 
# We saw how non-deterministic finite state machines can be converted to
# deterministic ones (often of a different size). It is also possible to
# simulate non-deterministic machines directly -- and we'll do that now!
#
# In a given state, a non-deterministic machine may have *multiple*
# outgoing edges labeled with the *same* character. 
#
# To handle this ambiguity, we say that a non-deterministic finite state
# machine accepts a string if there exists *any* path through the finite
# state machine that consumes exactly that string as input and ends in an
# accepting state. 
#
# Write a procedure nfsmsim that works just like the fsmsim we covered
# together, but handles also multiple outgoing edges and ambiguity. Do not
# consider epsilon transitions. 
# 
# Formally, your procedure takes four arguments: a string, a starting
# state, the edges (encoded as a dictionary mapping), and a list of
# accepting states. 
#
# To encode this ambiguity, we will change "edges" so that each state-input
# pair maps to a *list* of destination states. 
#
# For example, the regular expression r"a+|(?:ab+c)" might be encoded like
# this:
edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [4, 3],
          (4, 'c') : [5] }
accepting = [2, 5] 
# It accepts both "aaa" (visiting states 1 2 2 and finally 2) and "abbc"
# (visting states 1 3 3 4 and finally 5). 

def nfsmsim(string, current, edges, accepting):
	if string == "":
		return current in accepting
	elif (current, string[0]) not in edges:
		return False
	else:
		for state in edges[(current, string[0])]:
			if nfsmsim(string[1:], state, edges, accepting):
				return True
	return False

'''def nfsmsim(string, current, edges, accepting):
	if string == "":
		return current in accepting
	else:
		letter = string[0]
		if (current, letter) in edges:
			rest = string[1:]
			newStates = edges[(current, letter)]
			for newState in newStates:
				if nfsmsim(rest, newState, edges, accepting):
					return True
		return False'''

# This problem includes some test cases to help you tell if you are on
# the right track. You may want to make your own additional tests as well.

print ("Test case 1 passed: " + str(nfsmsim("abc", 1, edges, accepting) == True)) 
print ("Test case 2 passed: " + str(nfsmsim("aaa", 1, edges, accepting) == True)) 
print ("Test case 3 passed: " + str(nfsmsim("abbbc", 1, edges, accepting) == True)) 
print ("Test case 4 passed: " + str(nfsmsim("aabc", 1, edges, accepting) == False)) 
print ("Test case 5 passed: " + str(nfsmsim("", 1, edges, accepting) == False))

# ----------------------------------------------------------------------------------
#
# Title: Reading Machine Minds

# It can be difficult to predict what strings a finite state machine will
# accept. A tricky finite state machine may not accept any! A finite state
# machine that accepts no strings is said to be *empty*. 
# 
# In this homework problem you will determine if a finite state machine is
# empty or not. If it is not empty, you will prove that by returning a
# string that it accepts. 
#
# Formally, you will write a procedure nfsmaccepts() that takes four
# arguments corresponding to a non-derministic finite state machine:
#   the start (or current) state
#   the edges (encoded as a mapping)
#   the list of accepting states
#   a list of states already visited (starts empty) 
#
# If the finite state machine accepts any string, your procedure must
# return one such string (your choice!). Otherwise, if the finite state
# machine is empty, your procedure must return None (the value None, not
# the string "None"). 
#
# For example, this non-deterministic machine ...
edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [4, 2],
          (4, 'c') : [5] }
accepting = [5] 
# ... accepts exactly one string: "abc". By contrast, this
# non-deterministic machine: 
edges2 = { (1, 'a') : [1],
           (2, 'a') : [2] }
accepting2 = [2] 
# ... accepts no strings (if you look closely, you'll see that you cannot
# actually reach state 2 when starting in state 1). 

# Hint #1: This problem is trickier than it looks. If you do not keep track
# of where you have been, your procedure may loop forever on the second
# example. Before you make a recursive call, add the current state to the
# list of visited states (and be sure to check the list of visited states
# elsewhere). 
#
# Hint #2: (Base Case) If the current state is accepting, you can return
# "" as an accepting string.  
# 
# Hint #3: (Recursion) If you have an outgoing edge labeled "a" that
# goes to a state that accepts on the string "bc" (i.e., the recursive call
# returns "bc"), then you can return "abc". 
#
# Hint #4: You may want to iterate over all of the edges and only consider
# those relevant to your current state. "for edge in edges" will iterate
# over all of the keys in the mapping (i.e., over all of the (state,letter)
# pairs) -- you'll have to write "edges[edge]" to get the destination list. 

def nfsmaccepts(current, edges, accepting, visited): 
	if current in visited:
		return None
	elif current in accepting:
		return ""
	visited = visited + [current]
	for edge in edges:
		if edge[0] == current:
			for newState in edges[edge]:
				foo = nfsmaccepts(newState, edges, accepting, visited)
				if foo != None:
					return edge[1] + foo
	return None

# This problem includes some test cases to help you tell if you are on
# the right track. You may want to make your own additional tests as well.
print ("Test 1: " + str(nfsmaccepts(1, edges, accepting, []) == "abc")) 
print ("Test 2: " + str(nfsmaccepts(1, edges, [4], []) == "ab")) 
print ("Test 3: " + str(nfsmaccepts(1, edges2, accepting2, []) == None)) 
print ("Test 4: " + str(nfsmaccepts(1, edges2, [1], []) == ""))

