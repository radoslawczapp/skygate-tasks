# Task no. 2: "I write my programs in JSON"

While travelling, you have arrived at a small island somewhere in the middle of the ocean. You’ve got 
some problems with your visa, and you have to report to local authorities to pay a fine. As it turns out, 
they use an accounting software written by their (slightly eccentric) dictator, and the accountants have 
had a hard time getting their heads around it. They will be happy to forget about your fine if you help 
them to balance the books! 
 
The accounting software uses a peculiar storage format. They have a JSON document which contains a 
variety of things: lists (`[1,2,3]`), dictionaries (`{"a":1, "b":2}`), numbers, and strings. Your job is to simply 
find all of the numbers throughout the document and add them together. 

For example:
* `[1,2,3]` and `{"a":2,"b":4}` both have a sum of 6.
* `[[[3]]]` and `{"a":{"b":4},"c":-1}` both have a sum of 3.
* `{"a":[-1,1]}` and `[-1,{"a":1}]` both have a sum of 0.
* `[]` and `{}` both have a sum of 0.

#### Answer
Sum of all numbers: `111754`