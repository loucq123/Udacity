import random


def poker(handCards):
	"Return the best hand: poker([hand,...]) => hand"
	return all_max(handCards, key=hand_rank)

def all_max(iterable, key=None):
	"Return a list of all items equal to the max of the iterable"
	iterable.sort(key=key, reverse=True)
	result = [iterable[0]]
	maxValue = key(iterable[0]) if key else iterable[0]
	for value in iterable[1:]:
		v = key(value) if key else value
		if v == maxValue: 
			result.append(value)
		else: break
	return result


def hand_rank(handCard):
	"Return the rank of hand card: hand_rank([card,...]) => rank"
	suit = [s for r,s in handCard]
	#rank = ["--23456789TJQKA".index(r) for r,s in handCard]
	#rank = sorted(rank, reverse=True)
	count, rank = unzip(group(["--23456789TJQKA".index(r) for r, s in handCard]))
	if rank == [14, 5, 4, 3, 2]:
		rank = [5, 4, 3, 2, 1]
	straight = max(rank) - min(rank) == 4 and len(rank) == 5
	flush = len(set(suit)) == 1
	return (8 if straight and flush else
			7 if (4, 1) == count else
			6 if (3, 2) == count else
			5 if flush else
			4 if straight else
			3 if (3, 1, 1) == count else
			2 if (2, 2, 1) == count else
			1 if (2, 1, 1, 1) == count else
			0), rank
			
# the table-based lookup version:
# I will build it later for practice

def group(items):
	"Return a list of [(count, x), ...], highest count first, then highest x first"
	groups = [(items.count(item), item) for item in set(items)]
	return sorted(groups, reverse=True)

def unzip(iterable):
	"Return a list of tuples from a list of tuples : e.g. [(2,9), (2, 7)] => [(2, 2), (9, 7)]"
	return list(zip(*iterable))

myDeck = [rank + suit for rank in "23456789TJQKA" for suit in "SHCD"]
def deal(numberHands, n=5, deck=myDeck):
	random.shuffle(deck)
	return [deck[i*n:(i+1)*n] for i in range(numberHands)]

def test():
	"Test cases for the functions in poker game."
	sf1 = "6C 7C 8C 9C TC".split()
	sf2 = "6D 7D 8D 9D TD".split()
	fk = "9D 9H 9S 9C 7D".split()
	fh = "TD TC TH 7C 7D".split()
	tp = "5D 2C 2H 9H 5C".split()

	# Testing all_max
	assert all_max([2, 4, 7, 5, 1]) == [7]
	assert all_max([2, 4, 7, 5, 7]) == [7, 7]
	assert all_max([2]) == [2]
	assert all_max([0, 0, 0]) == [0, 0, 0]

	# Testing group
	assert group([2, 3, 4, 6, 2, 1, 9]) == [(2,2), (1,9), (1,6), (1,4), (1,3), (1,1)]
	assert group([8, 8, 8, 8]) == [(4, 8)]
	assert group([2, 6, 1]) == [(1,6), (1,2), (1,1)]

	#Testing unzip
	assert unzip([(2,2), (1,9), (1,6), (1,4), (1,3), (1,1)]) == [(2,1,1,1,1,1), (2,9,6,4,3,1)]
	assert unzip([(1,6), (1,2), (1,1)]) == [(1,1,1), (6,2,1)]
	assert unzip([(2,9), (2,7)]) == [(2,2), (9,7)]

	# Testing hand_rank
	assert hand_rank(sf1) == (8, (10,9,8,7,6))
	assert hand_rank(fk) == (7, (9,7))
	assert hand_rank(fh) == (6, (10,7))

	# Testing poker
	assert poker([sf1, fk, fh]) == [sf1]
	assert poker([fk, fh]) == [fk]
	assert poker([fh, fh]) == [fh, fh]
	assert poker([fh]) == [fh]
	assert poker([sf2] + 99*[fh]) == [sf2]
	assert poker([sf1, sf2, fk, fh]) == [sf1, sf2]

	return "tests pass"

if __name__ == "__main__":
	print (test())
