# import os

# if (not os.path.exists("day51.py")):
    # with open("day51.py",'w') as f:
        # pass # because i don't want ot write anything in this file right now.
    # print("success")

# f = open("day50.py",'w')
# f.write("'''The readlines() method reads a single line from the line .\n If we want to read multiple lines , we can use a loop.'''")
# f.close()

# with open("day51.py",'a') as f:
#     lines = ['f = open("day51.py",'r') \n ','while true: \n ','  line = f.readline()\n','  print(line)\n','  if not line: \n','    print(line, type(line))\n','    break']
#     f.writelines(lines)

# if (not os.path.exists("day56.py")):
#     with open("day56.py",'w') as f:
#         pass
#     print("success")

# import os
# # Path to the Semester-3rd directory
# semester_dir = r"F:\CODING\Semester-3rd"

# # Check if Semester-3rd exists
# if os.path.exists(semester_dir):
#      # Path for py3 directory inside Semester-3rd
#     py3_dir = os.path.join(semester_dir,"py3")

#      # Check if py3 doesn't exist, then create it
#     if not os.path.exists(py3_dir):
#         os.mkdir(py3_dir)
#         print("success")
#     else:
#         print("not success")
# else:
#     print("semester_dir does not exists")


# import os

# # Path to the Semester-3rd directory
# semester_dir = r"f:\CODING\Semester- 3rd"
# print(f"Checking path: {semester_dir}")  # Debug statement

# # Check if Semester-3rd exists
# exists = os.path.exists(semester_dir)
# print(f"Does semester_dir exist? {exists}")  # Debug output

# if exists:
#     # Path for py3 directory inside Semester-3rd
#     py3_dir = os.path.join(semester_dir, "py3")

#     # Check if py3 doesn't exist, then create it
#     if not os.path.exists(py3_dir):
#         os.mkdir(py3_dir)
#         print("success")
#     else:
#         print("not success")
# else:
    # print("semester_dir does not exist")


# import os

# folder = r"f:\CODING\Semester- 3rd\py3"

# exists = os.path.exists(folder)
# if exists:
#     question = os.path.join(folder,"que1.py")

#     if(not os.path.exists(question)):
#         # os.mkdir(question)
#         with open(question,'w') as f:
#             pass
#             print("success")
#     else:
#         print("not")

# else:
#     print("not exists")

import os

for i in range(58,101):
    if not os.path.exists(f"day{i}.py"):
        open(f"day{i}.py",'w')
        pass
        print("success")
