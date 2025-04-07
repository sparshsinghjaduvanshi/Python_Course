letter = "Hey my name is {1} and I am from {0} ."

country = "India"
name = "Sparsh"

# print(letter.format(country,name))#place variable in the sequence given in the above string .\
'''to prevent this we use number from 0 to place the variable at right order,
   like we 0 and 1 in the above string and the variable place at the right place ,
   even if they are in the wrong sequence by marking country as 0 and name as 1'''
# print(letter.format(name,country))

'''to resolve this issue we have a another way also ,
#    f-string .'''

# print(f"Hey my name is {{name}} and I am from {{country}} .")

price = 49.89999
txt = f"for only {price:.2f} dollors!"
txt1 = "for only {price:.2f} dollors!"
print(txt)
print(txt1.format(price = 49.899999))


