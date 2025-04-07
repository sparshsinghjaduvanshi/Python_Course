# Strings are immutable
a = "!!!!! Harry !!!!!!!! Harry !!!!!!!!!!"

# print(a.upper())
 
# a = a.lower()
# print(a.lower())
# print(a)

# print(len(a))
# print(a.rstrip("Harry"))#only which is present at last
# print(a.replace("Harry"," Sparsh"))# replace Harry with Sparsh
# print(a)
# print(a.replace("H"," S"))# replace Harry with Sparsh
# print(a.split("Harry"))#it makes a list of the string by adding commas inplace of the char you input

blogheading = "This IS my new channEl"
# print(blogheading.capitalize())#makes the first char captial and the rest small

# print(len(blogheading))
# print(len(blogheading.center(100)))#move the string to the center
# print(blogheading.center(50))
# print(blogheading)
# print(a.count("r"))#count how many times the character or word come in the string
# print(a.endswith("!!!"))# gives answer in boolean form
# print(a.endswith("!!!",5,20))# can also work in between strings from 5 to 20 index in this case

string = "I's am a boy, I am a student, he is also a student, my name is "
# print(string.find("jhguyjgg")) #only shows the index of first appearence and gives -1 if there is no occurance
# print(string.index("edhdf")) #only shows the index of first appearence and gives error if there is no occurance
# print(string[33])
# print(string[25])
str = "welcom to console"
# print(str.isalnum())
'''the isalnum() method returns True only if the entire string only consists of A-Z , a-z, 0-9. 
   If any other characters or punctions are present , 
   then it returns False
'''

# print(str.isalpha())
'''the isalpha() method returns True only if the entire string only consists of A-Z , a-z 
   If any other characters or punctions or numbers 0-9 are present , 
   then it returns False
'''

# print(str.islower())#True if all are in lower case

str = "welcom to console\n"
# print(str.isprintable())
'''true if all the values within the given string are printable ,
   if not then return False, e.g- \n
'''

s = " "
# print(s.isspace())#true if the string is only contain spaces

t = "Welcome To Console"
# print(t.istitle())#true if all first alphabet in the string is capital
# print(t.isupper())#true if all char in the string is capital
# print(t.islower())#true if all char in the string is lowercase
# print(t.startswith("Welcome"))#true if the stringss starts with the word or char that is given as input

# print(t.swapcase())#lowercase all uppercase and visa-versa.
# print(t.title())#uppercase all first alphabet in all the string.

'''To modify the string we can use :- '''
# import re

# a = "sparsh singh"
# a = re.sub("singh", "jaduvanshi", a)  # Replace "singh" with "jaduvanshi"
# print(a)  # Output: "sparsh jaduvanshi"


# first_name = "sparsh"
# last_name = "singh"
# new_last_name = "jaduvanshi"
# a = f"{first_name} {new_last_name}"
# print(a)  # Output: "sparsh jaduvanshi"


# a = "sparsh singh"
# a_list = list(a)  # Convert string to a list of characters
# a_list[7:] = list("jaduvanshi")  # Modify part of the list
# a = "".join(a_list)  # Join the list back into a string
# print(a)  # Output: "sparsh jaduvanshi"

# a = "sparsh singh"
# a = a[:7] + "jaduvanshi"  # Slice before "singh" and add "jaduvanshi"
# print(a)  # Output: "sparsh jaduvanshi"
