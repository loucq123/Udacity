##The Notes of Unit3

You can go to [Udacity CS262](https://www.udacity.com/wiki/cs262/unit-3) for more information.

###Context-free Grammars

This time we're going to move on to context-free grammars, the sentences of programming languages.

####Syntactic Structures

`wrote wrote simone de de de`. this sentence has no meaning, because they don't form a grammatical sentence.
We much prefer grammatical sentences.It's easier to interpret them and figure out what they mean.

    sentence → subject verb
     subject → teachers
     subject → students
        verb → write
        verb → think

Here these 5 lines together are my formal grammar, and each one is what is known as a rewrite rule.

sentence, subject and verb are called non-terminals. And you can rewrite it with whatever is to the right of the arrow.

teachers, students, write and think never occur on the left of any one of our rewrite rules, so they can neverr be replaced.Once you get there, you're stuck, and the process terminates. We call them terminals.

using these rules, if I start with sentence, I can rewrite sentence to be subject verb, and then I could rewrite that by picking any one of the rules that has subject on the left.

For the sentence `students think`, we can do this, `sentence → subject verb → students verb → student think`.
This sort of maneuver with all these arrows is sometimes called a derivation because I was able to derive "students think" starting from sentence using these rewrite rules.

####Infinity And Beyond

**Recursion** in a context-free grammar can allow for an infinite number of utterances.

I'm going to add just 1 rule, and that one itty bitty rule is going to give me phenomenal cosmic power. here I've added a rule to allow us to make compound subjects.

    subject → subject and subject

This rule uses recursion to define itself, it looks awesome. So we need a new derivation to derive this.

for `students and teachers think`,
`sentence → subject verb → subject and subject verb → students and subject verb → students and subject think → students and teachers think`

Here, we turned subject into **subject and subject**. And notice that now, rather than a 2-word sentence, we've produced a 4-word sentence.

This new power is called recursion in grammar. Here we can replace a non-terminal subject with that same non-terminal and some other stuff, so just as we might define define factorial in terms of factorial of x-1, we can define subject in terms of subject and subject.










