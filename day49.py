# f = open('myfile.txt','r')
# f = open('myfile.txt','rb')
# print(f) #not useful
# text = f.read()
# print(text)
# f.close()

# f = open('myfile.txt','w')
# f.write("HELLO WORLD!")
# f.close()

# f = open('myfile.txt','a')
# f.write("Hi my name is Sparsh Singh Jaduvanshi")
# f.close()

'''if I don't want to use the f.close() again and again then I can write it like as follows :- '''
with open('myfile.txt','r') as f:
    text = f.read()
    print(text)

