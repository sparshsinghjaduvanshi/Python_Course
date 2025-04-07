#COMMAND LINE UTILITY
'''these are programme that can be run from the terminal or
    command line interface,and they are an essential part of many 
    development workflows.In Python,you can create your own command
    line utilities using the built-in 'argparse' module.'''

'''SYNTAX :- '''
# import argparse
# parser = argparse.ArgumentParser()

# #add command line arguments
# parser.add_argument("arg1",help = "description of argument 1")
# parser.add_argument("arg2",help = "description of argument 2")

# #Parse the arguments
# args = parser.parse_args()

# #use the arguments in your code
# print(args.arg1)
# print(args.arg2)

'''EXAMPLE :- '''
# import argparse
# import requests

# def download_file(url,local_filename):
#     # local_filename = url.split('/')[-1]
#     #NOTE the stream = True parameter below.
#     with requests.get(url,stream = True) as r:
#         r.raise_for_status()
#         with open(local_filename,'wb') as f:
#             for chunk in r.iter_content(chunk_size=8192): 
#                 #If you have chunk encoded response uncomment if
#                 #and set chunk_size parameter to None.
#                 #if chunk:
#                 f.write(chunk)
#     return local_filename


# parser = argparse.ArgumentParser()

# #add command line arguments
# parser.add_argument("url",help = "URL of the file to download.")
# parser.add_argument("output",help = "by which name you want to save your file.")

# #Parse the arguments
# args = parser.parse_args()

# #use the arguments in your code
# print(args.url)
# print(args.output)
# download_file(args.url,args.output)


'''adding optional arguments :- '''

import argparse
import requests

def download_file(url,local_filename):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    #NOTE the stream = True parameter below.
    with requests.get(url,stream = True) as r:
        r.raise_for_status()
        with open(local_filename,'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                #If you have chunk encoded response uncomment if
                #and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
    return local_filename


parser = argparse.ArgumentParser()

#add command line arguments
parser.add_argument("url",help = "URL of the file to download.")
# parser.add_argument("output",help = "by which name you want to save your file.")
parser.add_argument("-o","--output",help = "name of the file.",default = None)#making it additional

#Parse the arguments
args = parser.parse_args()

#use the arguments in your code
print(args.url)
print(args.output)
download_file(args.url,args.output)





# to run this command in prompt we type ;- py day85.py {the url} {name we want it to save as}
# to run this command in prompt we type ;- py day85.py {the url} -o {name we want it to save as}#for optional
# https://www.shutterstock.com/image-photo/cpi-consumer-price-index-concept-wooden-2522263895