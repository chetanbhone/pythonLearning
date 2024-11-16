# validation for student name
while(True):
      name=input("enter your full name here")
      nameword=name.split()
      if(len(nameword)==0):
          print("dont enter spaces enter valid name")
      else:
          res=True
          for val in nameword:
              if(not val.isalpha()):
                  res=False
                  break
          if(res):
              break
          else:
              print("{} is invalid name".format(name))
