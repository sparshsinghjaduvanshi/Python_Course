#MULTIIPROCESSING IN PYTHON
'''is a python module that provides a simple way to run multiple processes in 
    parallel .It allows you to take advantage of multiple cores or processors
    on your system and can significantly improve the performance of your code.'''

'''to use it ew ned to create a process object  which calls a 
    start() method .The stat() method runs the process and them to stop
    the execution,we use the join() method .Here's how we can create a simple process.
'''
# import multiprocessing
# import requests

# def downloadfile(url,name):
#     print(f"starting downloading {name}")
#     response = requests.get(url)
#     with open(f"files/file{name}.jpg",'wb') as file:
#         file.write(response.content)
#     print(f"finished downloading {name}")

# if __name__ == '__main__':
#     url = "https://picsum.photos/200/300"
#     pros = []

# for i in range(5):
#     downloadfile(url,i)


import multiprocessing
import requests

def downloadfile(url,name):
    print(f"starting downloading {name}")
    response = requests.get(url)
    with open(f"files/file{name}.jpg",'wb') as file:
        file.write(response.content)
    print(f"finished downloading {name}")

if __name__ == '__main__':
    url = "https://picsum.photos/200/300"
    pros = []

    for i in range(5):
         # downloadfile(url,i)
         p = multiprocessing.Process(target = downloadfile,args = [url,i])
         p.start()
         pros.append(p)

    for p in pros:
        p.join()
