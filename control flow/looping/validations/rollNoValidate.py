# student roll number from range of 100 to 200
while("helo"):
   sNo=(input("enter your roll number here..."))
   if(sNo.isdigit() and (int(sNo) in range(100 , 201))):
       print("good")
       break
   print("{} is invalid roll number".format(sNo))
