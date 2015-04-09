##The Notes of Unit1##

You can go to [Udacity CS262](https://www.udacity.com/wiki/cs262/unit-1) for more information.

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

4/8/2015 11:03:37 PM

It turns out that Python's regular expression module actually uses something very similar to FSM simulator.
However, our simulation didn't handle**epsilon transitions** or **ambiguity**, and what I mean by ambiguity is what if there are 2 outgoing edges labeled a?
So, ambiguity means that I can go to 2 different places on the same input --are formerly known as non-deterministic finite state machines.

###Save the World###

Let's wrap up what we've learned in this unit.

Strings are just sequences of characters, and manipulating strings is going to be crirically important for making a web browser.

Modern programming languages support regular expressions, which are just a concise notation for specifying sets of strings, and using regular expressions is more flexible than using fixed string matching like `string.find()`.

Wigh regular expressions, we can define phone numbers, words, numbers, quoted strings, and given a regular expression, we can search for and match it in a bigger string.

**Finite state machines** are pictorial equivalent to regular expressions.

Every regular expression, concatenation, plus, question mark, star, has an equivalent finite state machine.

*Every regular expression has a finite state machine, and every finite state machine has a regular expression*.

And then every finite state machine can be converted to a **deterministic** finite state machine.

Once we have a deterministic finite state machine, we can simulate it, and it turns out it's very easy--about 10 lines of recuresive code--to see if a deterministic finite state machine accepts a string.

###Conclusion###

We've just finished learning about sets of strings, regular languages, regular expressions, and finite state machines, a beautiful formalism and a lovely way of implementing it in actual Python.

This idea, this tool of regular expressions specifying sets of strings is a really powerful and really expressive way of writing quite a few programs.

We're going to see this come up later on in everything from mail to web servers to web browers to writing our interpreter for **JavaScript** and **HTML**.

By Lou Chaoqi

4/9/2015 12:43:44 PM 