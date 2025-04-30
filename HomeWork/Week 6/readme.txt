🔟 Binary conversion table
In everyday life we represent numbers in decimal using the digits 0, 1, 2, ..., 9. On the other hand, computers often represent numbers in binary using only ones and zeros. When working with computers it might be useful to have a reference table to convert between binary and decimal representations of whole numbers (integers), like this:

00000000 is 0
00000001 is 1
00000010 is 2
00000011 is 3
Write a program which saves a binary conversion table like that shown above to a file called table.txt. The program accepts two integers as input: the starting number (start) and the stopping number (stop). The binary conversion table should have a row for each integer i starting with start and going up to (but not including) stop. The above output is for when start is 0 and stop is 4. Note that the binary number should have leading zeros to ensure that it is at least 8 digits wide.

The easiest way to construct the rows of the output table is to use an f-string to format each line. Conveniently, there is a b presentation type which displays an integer in binary (just like d displays an integer in decimal).

But what about the leading zeros? You have already learnt how to specify the width (in characters) when formatting a value. However, by default the desired width is achieved using spaces for padding, not zeros. To specify that an integer should be padded with zeros instead of spaces, include 0 before the width. For example, print(f'{42:04d}') produces 0042 instead of ␣␣42. This works with the binary presentation type too.