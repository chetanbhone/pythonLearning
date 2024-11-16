# program for check eligibility of citizen to vote or not
while(True):
    age=int(input("what is your age"))
    if(age>=18):
        print("congrats you are eligible for vote")
        break
    else:
        print("-"*40)
    print("{} years prople not eligible for vote".format(age))