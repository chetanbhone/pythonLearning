# generating student report program
# validation for student number
while(True):
    sNo=input("enter your number here")
    if(sNo.isdigit() and int(sNo) in range(100,201)):
        break
    print("{} is invaid number".format(sNo))
# validation for student name
while True:
    name = input("Enter your full name here: ")
    nameword = name.split()

    if len(nameword) == 0:
        print("Please enter a name, not just blank spaces.")
    else:
        res = True
        for val in nameword:
            if not val.isalpha():  # Corrected 'isalpha' spelling
                res = False
                break
        if res:
            break  # Breaks out of the loop if the name is valid
        else:
            print("{} is invalid input.".format(name))

# validation for marks for cpp
while(True):
    cpp=input("enter your marks here for cpp")
    if(cpp.isdigit() and int(cpp) in range(1,101)):
        break
    print("{} is invalid marks enter it again".format(cpp))

# validation for marks for pym
while(True):
    pym=input("enter your marks here for python")
    if(pym.isdigit() and int(pym) in range(1,101)):
        break
    print("{} is invalid marks enter it again".format(pym))

# validation for marks for java
while(True):
    java=input("enter your marks here java")
    if(java.isdigit() and int(java) in range(1,101)):
        break
    print("{} is invalid marks enter it again".format(java))

# calculate marks and percentage
totMarks=int(cpp)+int(pym)+int(java)
percent=(totMarks/300)*100

# code for student getting PASS or FAIL
if((int(cpp) or int(pym) or int(java))<40):
    grade="FAIL"
else:
    if(totMarks in range(250,301)):   # method 1 for condition
        grade="DISTINCTION"
    elif(200<=totMarks<=249):         # method 2 for condition
        grade="FIRST"
    elif(totMarks>=150 and totMarks<=199):          # method 3 for condition
        grade="SECOND"
    elif(totMarks in range(120,150)):             # method 4 for condition
        grade="THIRD"
print("-"*40)
print("student marks report")
print("-"*40)
print("student number :{}".format(sNo))
print("student name :{}".format(name))
print("student marks in cpp :{}".format(cpp))
print("student marks in python :{}".format(pym))
print("student marks in java :{}".format(java))
print("-"*40)
print("student total marks :{}".format(totMarks))
print("student percentage :{}".format(percent))
print("student grade : {}".format(grade))
print("-"*40)