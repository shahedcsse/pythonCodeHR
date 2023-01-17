std=[1,2,34,54,55,7,"red",]
print(std)

#List
#last index add value
std.append(22)
#ispacific index add 
std.insert(1,65)
#cheek index number
std.index(54)
#count 
std.count(34)

# add multipul value
std.extend([90,10,30])
#pop list of last value
std.pop()
#ispacific number of pop
std.pop(3)
#remove number
std.remove("red")
#sort acending order
std.sort()
#sort revers
std.sort(reverse=True)
#revers function
std.reverse()
#anoder type of reverse
std[::-1]
#update the value
std[2]= 0
#multipul vale update
std[2:5]=0,-1,0
#clear
#std.clear()

#shallow copy vs deep copy
std1=std
std1.insert(2,"shallow copy")
print(std1)

'''deep copy  no changes
std2=std.copy
std2.insert(4,"deep copy")
print(std)'''
p="python"
list(p)
print (list)

'''List []
   Tuple ()
   set {}
'''

#set function no duplicat value
s1 ={1,2,3,43,33,3,2,12,31,33}
#pop
s1.pop()
print(s1)
#s1.add(23)
print(s1)

#Dictionary

data={"roll":1,"name":"shahed","age":25}
#update roll
data['roll']=2
#update new value
data['branch']="ces"
data.update({44:444})
#defult value add
data.fromkeys([2,3,4,5,6,7],333)
print(data)
data.items()
print(data)


