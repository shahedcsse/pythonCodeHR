try:
    num=5
    r=num/0 +"str"
except ZeroDivisionError as e: 
    print (e)
except TypeError as e:
    print (e)

finally:
    print("finally")           
    print ("welcome")