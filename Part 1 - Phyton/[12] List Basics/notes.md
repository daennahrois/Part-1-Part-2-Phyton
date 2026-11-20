01. Create a List

A list is an ordered collection of items, and we write it inside square brackets with
commas between the items. A list can hold text, numbers, True or False values, and
decimals, even all in the same list. We can also create an empty list with nothing inside,
and fill it later. Python has a built-in function called type() that tells us what kind of data
something is. For our list, it will say list .

02. Access List Items

Every item in a list has an index, which is its position number. The first item is at index 0,
the second at index 1, and so on. Python also lets us count from the end using negative
numbers. Index -1 is the last item, and -2 is the second to last. If we want more than one
item, we can use slicing. A slice has a start and a stop, written with a colon. The start is
included, but the stop is not.

03. Change a List Item

Lists are mutable, which means we can change them after they are created. To change
one item, we assign a new value to its index. This works with negative indexes too. We can
also replace several items at once by assigning a list to a slice. The old items are removed
and the new ones take their place.

04. List Length

The len() function tells us how many items are in a list. It works for any list, even an
empty one, and it always gives the current size. If we add an item, the length goes up.
Knowing the length is also useful for finding the last index, because the last index is
always the length minus one.

05. Loop Through a List

A loop lets us do something for every item in a list. The simplest way is the for loop, where
Python gives us one item at a time. If we also need the position number, we have two
choices. We can loop over range(len(list)) to get the indexes, or use enumerate() to
get the index and the item together. There is also the while loop, where we manage the
counter ourselves. For most cases, the plain for loop is the cleanest.

06. Check if an Item Exists in a List

Sometimes we need to know if a value is in a list before we use it. The in keyword checks
this and gives back True or False. The opposite is not in . We usually combine these with
an if statement. If we also want the position of the item, we can use the index() method,
but only after we confirm the item exists, because index() gives an error when the item
is missing.

07. Sum of List Numbers

Adding up the numbers in a list is a very common task. The manual way uses a loop with a
variable called total, which starts at zero. For each number, we add it to the total. This
pattern is called an accumulator. Python also has a built-in sum() function that does the
same job in one line. Once we have the total, we can find the average by dividing by the
number of items, which we get from len().

08. Find the Highest Score

To find the highest value, we can use a loop. We assume the first item is the highest, then
check every item. If we find a bigger one, it becomes the new highest. At the end, the
variable holds the biggest value. We can find the lowest value the same way by reversing
the comparison. Python also has max() and min() as shortcuts. And if we have a second
list with names in the same order, we can use index() to find the name that belongs to
the top score.