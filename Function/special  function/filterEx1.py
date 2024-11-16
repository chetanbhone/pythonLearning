# filter function to filter out the postive and negative element from list
# function for filter positive
def pos(val):
    if(val>0):
        return True
# function for filter out negative
def neg(val):
    if(val<0):
        return True

# main program
lst = [int(val) for val in input().split()]  # list compression
pslist=list(filter(pos,lst))
nglist=list(filter(neg,lst))
print(pslist,type(pslist))
print(nglist,type(nglist))







