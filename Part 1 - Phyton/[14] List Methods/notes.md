01 - Append an Item

append() adds one new item at the very end of a list. It changes the original
list, so we do not need to save the result in a new variable.

02 - Insert an Item

append() always adds at the end. If you want to add an item at a specific
position, use insert() . It needs two things: the index where the item should go, and the
item itself.

03 - Remove an Item

remove() deletes an item by its value, not by its index. Important: it removes
only the first match. And if the value is not in the list, Python raises an error, so it is a good
habit to check with in first.

04 - Pop an Item

pop() removes an item by its index and also gives that item back to you, so
you can store it in a variable. If you do not give an index, it removes the last item.

05 - Sort a List

sort() arranges the items in order. By default it goes from smallest to
largest, orA to Z for text. Add reverse=True to go the other way. Remember: sort()
changes the original list. If you want to keep the original, use the function sorted() ,
which gives you a new list.

06 - Reverse a List

reverse() flips the order of the list. It does not sort anything. It simply
turns the list backwards. Like sort() , it changes the original list. If you want a reversed
copy, you can use slicing with [::-1] .

07 - Count and Index

count() tells you how many times a value appears. index() tells you the
position of the first match. Be careful: if the value is not in the list, index() gives an error,
so check with in first. count() is safe, because it just returns 0.

08 - Use sum(), min(), and max()

These are functions, not methods. We do not use a dot. We put the list inside
the parentheses, like sum(my_list) . sum() adds all numbers, min() finds the smallest,
and max() finds the biggest. Together with len() , we can compute the average.