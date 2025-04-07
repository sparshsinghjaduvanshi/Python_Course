#REGULAR EXPRESSION
'''regex for short, are a powerful tool for working wit strings
    and text data in python .They allow you to match and manipulate 
    strungs based on patterns,making it easy to perform complex string
    operations with just a few lines of code.'''

#META-CHARACTERS IN REGULAR EXPRESSIONS

'''
[] - REPRESENT A CHARACTER CLASS
^  - MATCHES THE BEGINING
$  - MATCHES THE END
.  - MATCHES ANY CHARCTER EXCEPT NEWLINE
?  - MATCHES ZERO OR ONE OCCURANCE
|  - MEANS OR (MATCHES WITH ANY OF THE CHARACTERS SEPERATED BY IT)
*  - ANY NUMBE OF OCCURENCES
+  - ONE OR MORE OCCURENCES
{} - INDICATES NUMBER OF OCCURANCES OF A PRECEDING RE.'''


import re
#Define a regular expression pattern
pattern = r"[A-Z]+indows"

#Match the pattern against a string
text = '''Eyewitness A. D. Singh reported that he had seen the fire begin as 
          a result of a dropped cigarette, whilst Safi Pitoliwali claims he
          saw electrical wiring in the toilet WInDoWs of the fourth carriage catch alight,
          but what ever the Windows cause, the speed of the train combined
          with the open Findows during the Indian summer to create 
          an inferno, as air carried the fire back 
          through three carriages in a massive burst of flame.
'''

# match = re.search(pattern,text)#find the first occurance.
# print(match)

matches = re.finditer(pattern,text)
for match in matches:
#     print(match)
    print(match.span())
#     print(type(match.spn()))
    print(text[match.span()[0]:match.span()[1]])  
