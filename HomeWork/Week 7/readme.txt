📝 Bag of words
Software that tries to understand and work with normal written text is said to perform "natural language processing" (NLP). Some NLP algorithms treat a sentence as a "bag of words", which is an unordered collection of unique words that make up the sentence. Additionally, stopwords with little meaning such as "a", "the", "in", etc. are excluded from the bag of words.

For the purposes of this exercise we will consider the following words to be stopwords:

a       an      the     as
at      by      for     in
of      on      to
Your task is to take a sentence input by the user and output the size of the bag of words representing that sentence. For example, if the user inputs "bumper to bumper traffic" then the bag of words contains "bumper" and "traffic", so the output of the program should be 2.

You may assume that the input sentence contains lower-case letters and spaces only. To split the sentence into a list of words, use the split() string method. Here's an example of using the split() method on a string literal:

>>> 'bumper to bumper traffic'.split()
['bumper', 'to', 'bumper', 'traffic']
