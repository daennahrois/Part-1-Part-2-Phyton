01. Create a Nested List

A nested list is created by putting lists inside another list. The outer list holds the rows,
and each inner list is one row. When every inner list has the same size, we get a matrix, like
a table with rows and columns. The inner lists can also hold different kinds of data, like a
name and a score. We can use len() to count the rows, and len() of one row to count
the columns.

02. Access Items in a Nested List

To get an item from a nested list, we use two indexes. The first index picks the row, and
the second index picks the item inside that row. If we use only one index, we get a whole
row. Both indexes start at zero. Negative indexes also work, so -1 means the last one.


03. Loop Through a Nested List

To go through a nested list, we use a loop. A single for loop gives us one row at a time. If we
want every individual value, we put a second for loop inside the first one. That is called a
nested loop. There is also a way to loop using the index numbers, with range(len(...)) .
This is useful when we need to know the exact position of each value.

04. Display a Matrix

When we print a nested list directly, it looks messy. A matrix looks better if each row is
printed on its own line, with the numbers side by side. To do that, we change the end of
the print function. By default, print ends with a new line. If we set end to a space or a tab,
the numbers stay on the same line. Then, after each row, we use an empty print() to
move to the next line. There is also a shortcut using the join() method.

05. Sum ofAll Items in a Nested List

To add up all the numbers in a nested list, we use a nested loop and an accumulator called
total. The total starts at zero, and every value is added to it. We can also use the sum()
function on each row, so we only need one loop. Once we have the total, we can count the items and compute the average.

06. Find an Item in a Nested List

To search for a value in a nested list, we check every item with a nested loop. When we
find it, we print its row and column. Then we can stop early using break . The problem is
that break only stops the inner loop. So we use a variable called found, and after the
inner loop we check it to stop the outer loop too. We can also search a list of records, like
names and scores, by checking the first item of each row.

07. Row Totals and Column Totals

With nested lists, we often need totals for each row and each column. Row totals are easy,
because each row is already a list. Column totals need a little more thinking. We loop
through the column numbers, and for each column we go through every row and add the
value at that column. We can also compare the row totals to find which row has the
highest total.

08. Nested List as a Table

Our last program shows a nested list as a real table. Each inner list is a record. The first
item is the name, and the rest are scores. We print a header, then one line for each
student, and we compute each student's average using slicing. To keep the columns lined
up, we use f-string formatting, where the colon, a less-than sign, and a number set the
width of each column. Finally, we find the student with the best average.