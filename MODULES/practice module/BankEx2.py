def simpleInt(name , add):
    p=int(input("enter principle amount here"))
    r= float(input("enter rate of intrest here"))
    n=int(input("enter time here"))
    si=(p*r*n)/100
    totalAmount=si+p
    print("for the Bank {} at {}".format(name,add))
    print(" the principle amount {} \n and rate of intrest {} \n for the time {} \n".format(p,r,n))

    print("-"*40)
    print("the simple intrest is {}".format(si))
    print("total value is {}".format(totalAmount))
    print("-"*40)
