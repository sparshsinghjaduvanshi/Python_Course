'''dictionaries are odered collection of data items. They store multiple items in a single variable.
    Dictionary items are key-value pairs that are seperated by commas and enclosed with curly braces {}.'''

# dic = { "harry" : "Sparsh", "python" : "Singh"} 
'''here python and harry are the key words and the adjacent strings are the values .'''

# print(dic["harry"])

dic1 = {1:"sparsh", 2: "singh", 3:"jaduvanshi", 4:"SURYA"}
# print(dic1[1])
# print(dic1)
'''there are two ways to address the values of the dic. '''
# print(dic1[3])#throughs error if the value not found
# print(dic1.get(3))#give none as output if the keyword is not present

'''addressing multiple variable'''
# print(dic1)
# print(dic1.keys())#for all keys
# print(dic1.values())#for all variables
# print(dic1.items())#to print dic. with key values pair.

# for keys in dic1.keys():
#     print(dic1[keys])