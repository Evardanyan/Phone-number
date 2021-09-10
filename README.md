# Phone-number
Check phone numbers with regex


Phone numbers
Besides our love for email adress matching, another funny (i.e. most common) application of regular expressions is phone number extraction. Your task is to write a program that will take a string as an input and match the phone numbers. The output should be of the following format:

Full number: +1-234-567-8900
Country code: 1
Area code: 234
Number: 567-8900
If no matches are found, the program should return No match.

Note that instead of a dash -separating the numbers there might be a whitespace or no separators at all. The phone numbers always start with +.


Sample Input:
+1-234-567-8900

Sample Output:
Full number:  +1-234-567-8900 
Country code:  1 
Area code:  234 
Number:  567-8900
