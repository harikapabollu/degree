#id=input('enter id name')
#pw=input('enter password')
#if id=='thub' and pw=='1234':                          ##### task #####
   # print('login')

#else:
    #print('wrong credentials')
    


#s=int(input('enter a start number'))

##i=0
##while True:
##      i+=1
##      print(i)
##      if i==10:
##            break
      
      
###nearest prime--> 3 5 7  10 11 13

##from math import sqrt
##def is_prime(n):
##    s=int(sqrt(n))
##    for i in range(2,s+1):
##        if n%i==0:
##            return False
##        return True
##def right_prime(n):
##    i=n+1
##    while 1:
##        if is_prime(i):
##            return i
##        i+=1
##def left_prime(n):                                        ##### nearest prime #####
##    j=n-1
##    while 1:
##        if is_prime(j):
##            return j
##        j=j-1
##def near_prime(n):
##    if is_prime(n):
##        return n
##    else:
##        x=right_prime(n)
##        y=left_prime(n)
##        if abs(n-x)<abs(n-y):
##            print(x)
##        elif abs(n-x)>abs(n-y):
##            print(y)
##        else:
##            print(x,y)
##n=10
##near_prime(n)


##n=int(input('enter a number'))
##for i in range(1,n+1):#1                      ##### pattern #####
##    for j in range(1,i+1):#1:1,2
##        print('*',end=" ")
##    print()


##n=int(input('enter a number'))
##for i in range(65,65+n):                  #### own programe ####
##    for j in range(65,i+1):             
##        print(chr(j),end=" ")
##    print()
    

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(n-i,0,-1):
        print('*',end="")
    print()



























        
        
