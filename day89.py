#REQUEST MODULE
'''the Python request module is an HTTP library that enables
    developers to send HTTP requests in Pthon .This module 
    enables yo to send HTTP requests using python code and makes it possible to interact 
    with API's and web servics.'''


#GET request:-
# '''simple example that sends a GET request to the GOOGLE homepage. '''
# import requests

# response = requests.get("https://www.google.com")
# print(response.text)

#POST request :-

# import requests

# # response = requests.get("https://www.google.com")

# url = "https://jsonplaceholder.typicode.com/posts"

# data = { "title" : 'foo',
#          "body" : 'bar',
#          "userid" : 1
#          }

# headers = {'content-type' : 'application/json; charset = UTF-8'}

# response = requests.post(url,headers=headers,json=data)

# print(response.text)


'''there is another module named BeautifulSoup(bs4) which is used for web 
    scraping in Python.
    
    It is used for polling data out of HTML and XML files.It
    works with your faviourite parser to provide kilomatic ways of 
    navigating,searching and modifing the parse tree. It commmonly saves
    programmers hours or days of work.'''

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')

# print(soup.prettify())
for heading in soup.find_all('div   '):
    print(heading.text)