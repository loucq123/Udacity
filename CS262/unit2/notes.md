##The Notes of Unit2##

You can go to [Udacity CS262-Unit2](https://www.udacity.com/wiki/cs262/unit-2) for more information.

In this unit, we will learn how to make a lexical analyzer--a program that reads in a web page or a bit of JavaScript and breaks it down into words, just like I might break English sentence down into words.

###HTML Fundamentals###

**HTML** stands for the "hypertext markup language." HTML was invented by Tim Berners-Lee, a British computer scientist working in Switzerland around 1990.

####Tags####

`<b>`, `</b>`, `<u>`, `</u>`, `<i>`, `</i>`, these are all tags. And they tell you how to display words.

But a super common kind of tag, anchor tag `<a>` is a little different. It is used to add hyperlinks to webpages.

For example, `Click here <a href="www.google.com"> now! </a>`.
It begins with `<a`, unlike the relatively simple bold and underline tags, it has an **argument**.This means pretty much the same thing it did when we were talking about functions in Python or math. In `sin(pi)` the argument of my sine function is `pi`. Here the argument or modifier for my anchor tag is `href=`. This stands for **hypertext reference**--the target of this link.
After `href=` We have a string that is a URL, a web address. Hypertext transfer protocol google.com. This text in the middle is oftern rendered in blue with an underline, although it doesn't have to be. With `</a>` We're ending the anchoring tag. 

The syntax `<a` marks the beginning of the anchor tag. The syntax `</a>`, marks the end of the anchor tag. This part `href="www.google.com"` is the argument of the tag. It contains extra information for things that are more complicated than simple bold or underline.

In order to interpret HTML and JavaScript, We're going to have to vreak sentences down into their component words to figure out what's going on. This process is called **lexical analysis**. Lexical here has the same roots and "lexicon" like a dictionary. This means "to break something down into words." We are going to use regular expressions to solve this problem.

###Some Knowledge of ply

When two token definitions can match the same string, the behavior of our lexical analyzer may be ambiguous. And we're going to use a very simple rule to avoid **ambiguity**.The first one you list wins, the one closer to the top of the file, so this is our big winner and is going to take priority over string.

You can go to here[GitHub/loucq123](https://github.com/loucq123/Udacity/blob/master/CS262/unit2/learn_ply.py) to see some code about using ply to construct a lexan.

tomorrow's tasks: keeping going, complete unit3

By Lou Chaoqi

4/9/2015 11:14:55 PM 



