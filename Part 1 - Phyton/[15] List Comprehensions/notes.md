01. Squares

Let us start with the basic syntax. In square brackets we write an expression, then for,
then a variable name, then in, then something we can loop through, like range(). The
expression is the value that goes into the new list. Here, we will square each number. We
will also write the same program with a regular for loop so we can compare them.

02. Create Even Numbers

A list comprehension can also have a condition at the end. We write if after the loop, and
only the items that pass the condition are added. To check if a number is even, we use the
modulo operator. If a number divided by 2 has a remainder of 0, it is even. We will also see
another way to get even numbers, by using an expression.

03. Uppercase Words

List comprehensions work with lists of strings too. We can call a string method on every
item. Here, we use the upper() method to change every word to uppercase. Remember,
the original list is not changed. We get a brand new list.

04. Filter Long Words

Now let us filter a list of strings. We can use the len() function inside the condition to
check the length of each word. Only the words that pass the condition are added to the
new list. Notice that the expression is just the word itself, because we want to keep the
word as it is.

05. Convert Temperatures

The expression can be a full formula. Here we convert a list of temperatures from Celsius
to Fahrenheit. The formula is Celsius times 9 divided by 5, plus 32. The list comprehension
applies this formula to every temperature and gives us a new list of results.

06. Label Numbers

So far, the if was at the end of the list comprehension, and it removed items. But what if
we want to keep every item and just change it based on a condition? For that, we use an if-
else inside the expression, at the front. This is called a conditional expression. The pattern
is: value if condition else other value, then the for loop.

07. Flatten a Nested List

A list can contain other lists. This is called a nested list. A list comprehension can have
more than one for. When we do that, the loops run in the same order as if we wrote them
as nested for loops, from left to right. We can use this to flatten a nested list into one
simple list.

08. Words Starting with a Vowel

For our last program, let us combine what we learned. We will go through a list of words
and keep only the words that start with a vowel. To get the first letter of a word, we use
index 0. Then we check if that letter is inside the string of vowels using the in keyword.
We also use lower() so that capital letters work too.