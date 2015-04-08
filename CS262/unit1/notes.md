##The Notes of Unit1##

###Regular Expressions###

Regular expressions are tools that give you more control over splitting up strings.

When you use Python, you could import the **re** module.

For how to use re, you can see it in learn_re.py.

### Finite State Machines###

FSM is a visual representation for regular expressions that actually shows exactly what's going on behind the scenes.

- start
- state
- edge
- accepting state

**start** is an arrow coming out of nowhere on the left that's not connected to the rest of the picture.

**state** represents what we're up to when we're matching a string.

**edge** tells us when to move one state to another.

**accepting state** is the end of finite state machine.

####FSM Simulator####

In Python, we can encode our finite state machine using a **dictionary**.

The **key** is a tuple containing **currentState** and **input**, and **value** is the **nextState**.

For example, in `r"a+1+"`, we can encode as following:`edges = {(1, 'a'): 2, (2, 'a'): 2, (2, '1'): 3, (3, '1'): 3}`.Is this really easy?

Tasks for tomorrow: do some interesting quizzes!

By Lou Chaoqi

4/8/2015 11:03:37 PM


