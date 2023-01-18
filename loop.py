# For Loop
for i in(1,3,3,4,6,3,6,7,2):
    print (i)
    
print("set")

for j in {2,1,3,3,4,6,3,6,7,2}:
    print (j)

print("dic")    

for key,value in {"a":3,"b":6,"c":7}.items():
    print(key ,"=>",value)

#matrix

data=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]    
for row in data:
    for colam in row:
     print(colam)

#range 

ra=list(range(1,10))
print(ra)

ra=list(range(1,10,2))
print(ra)
#reverse range
ra=list(range(10,1,-1))
print(ra)

#range for loop[]

for num in range(1,10):
    print(num**2)

# list comprehance
#    
power=[]
for num in range(1,10):
    if num%2==0:
        power.append(num**2)
    else:
        power.append(num**3)
print(power)

#list copre
print("comprehance")
powerlist=[num**2 if num%2==0 else num**3 for num in range(1,10)]   
print(powerlist)    


#function


def good():
    print("welcome ")
good()    

#function arg 
def is_even(num):
    if num%2==0:
        print(True)
    else:
        print(False)
is_even(5)            