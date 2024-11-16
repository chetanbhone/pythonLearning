def dispInfo(sno,name,marks,course="java"):
    print("\t\t{}\t\t{}\t\t{}\t\t\t{}".format(sno,name,marks,course))
print("-"*40)
print("\t\tSNO\t\tname\t\tmarks\t\tcourse")
dispInfo(123,"Radha",100)
dispInfo(123,"Radha",100,"C++")
dispInfo(course="Ruby",sno=123,name="Radha",marks=100)
dispInfo(123,"Radha",100,"HTML")
print("-"*40)