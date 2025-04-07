'''The readlines() method reads a single line from the line .
 If we want to read multiple lines , we can use a loop.'''

# f = open('myfile.txt','r')
# while True: 
#     line = f.readline()
#     print(line)
#     if not line: 
#         print("line", type(line))
#         break

# line = f.readline()
# print(line)
# f.close()

# f = open('myfile.txt','r')

# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"The marks of the student number {i} is {m1}.")
#     print(f"The marks of the student number {i} is {m2}.")
#     print(f"The marks of the student number {i} is {m3}.")
#     print(line)

# f.close()

'''the writelines() method in python writes a sequence of strungs to a 
    file. The sequence can be any iterable opject, such as a list or a tuple.'''

# f = open('myfile.txt','w')

# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close()

'''keep in mind that the writelines() metthod does not add newline 
    characters between the strings in the sequence .
    If ypu want to add nelines between the string you can 
    use loop to write each string seperately.'''

f = open('myfile.txt','w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line+'\n')
f.close()