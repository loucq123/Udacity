# quiz: FSM Simulator

# Define edges and accepting. Name your start state 1

edges1 = {(1, 'a'): 2, (2, 'a'): 2,
         (2, '1'): 3, (3, '1'): 3}
accepting1 = [3]
# corresponds to r"a+1+"
def fsmSimulator1(string, current_state, edges, accepting):
    if string == "":
        return current_state in accepting
    else:
        letter = string[0]
        if (current_state, letter) in edges:
            return fsmSimulator1(string[1:], edges[(current_state, letter)], edges, accepting)
        else:
            return False

# test
assert (fsmSimulator1("a11", 1, edges1, accepting1)) == True
assert (fsmSimulator1("aaac1", 1, edges1, accepting1)) == False

# quiz: FSM Interpretation

edge2 = {(1, 'q'): 1}
accepting2 = [1]
# corresponds to r"q*"

def fsmSimulator2(string, current_state, edge, accepting):
    if string == "":
        return current_state in accepting
    else:
        letter = string[0]
        if (current_state, letter) in edge:
            new_state = edge[(current_state, letter)]
            remain_string = string[1:]
            return fsmSimulator2(remain_string, new_state, edge, accepting)
        else:
            return False
# test
assert (fsmSimulator1('', 1, edge2, accepting2)) == True
assert (fsmSimulator1('q', 1, edge2, accepting2)) == True
assert (fsmSimulator1('qq', 1, edge2, accepting2)) == True
assert (fsmSimulator1('p', 1, edge2, accepting2)) == False


