import re


print (re.findall(r"[a-c]", "lou chaoqi"))

                    # Concatenation

print (re.findall(r"[a-c][1-2]", "a1a3 c2c1bb2"))

# 12 is a two-digit number, 34 is a two-digit number, but 5 actually does not qualify.
# This regular expression requires that both subparts be matched
print (re.findall(r"[0-9][0-9]", "12345"))

                    # One or more

print (re.findall(r"[0-9]+", "13 from 1 in 1776"))

                    # Disjunction

print (re.findall(r"[a-z]+|[0-9]+", "HellOloucq123"))

                    # Optional

print (re.findall(r"-?[0-9]+", "100-23"))

                    # Just as we can get a lot of use out of + for 1 or more copies,
                    # sometimes it's nice to have 0 or more copies.
                    # So we'll introduce the * regular expression for that.

print (re.findall(r"-?[0-9][0-9]*", "100-23"))

                    # How to deal with special characters

print (re.findall(r"\+", "3+4"))
print (re.findall(r"\\", "\ssd"))    # I don't know why the output is '\\'

                    # Dot(.)

print (re.findall(r"[0-9].[0-9]", "2v2 333 sc2"))
print (re.findall(r"[0-9]+\.[0-9]+", "2.344sdf13.98"))   # comparison

                    # Caret(^)

print (re.findall("[0-9][^a-b]", "1a1 222 2cc3"))
# Here we've got a 2 and a space, and this space is not 'a' or 'b', so that looks good.

print (re.findall("[0-9][^a-b]", "1a1 2222cc3"))
print (re.findall("[0-9][^a-b]", "1a1 222 cc3 4c"))

                    # Parenthesis

print (re.findall("(?:xyz)+", "xyzyxyz"))

print (re.findall(r"do+|re+|mi+", "mimi rere midore doo-wop"))   # wrong!
print (re.findall(r"(?:do+|re+|mi+)+", "mimi rere midore doo-wop"))  #correct!



