import numpy as np


####### Basic Operations ####### 
a=2
b=3
print('a+b=',a+b)
print('a*b=',a*b)
print('a^b=',a**b)
print('a/b=',a/b)
c=a+b
b=5
print('c=',c)
print('new b=',b)



########lists#########

#how to define a list
print('LISTS')
L=[] #empty list
M=[1,2,3] #define a list with elements

#add element to list L
L.append(3) #qdd integers
L.append('hello') #add strings
L.append(M) #add list
L.append(42.5) #add float
L.append(True) #add boolean

print(L) #as you can see, a list can contain different sort of objects

#operations on lists
print('L*2=',L*2) 
print('L+M=',L+M)
print('[0]*5',[0]*5)

#access to an element
a=L[0]
b=L[2]
c=L[-1]
d=L[-2]
print('a=',a,'b=',b,'c=',c,'d=',d)
#lenght of a list :
print('in L, there are ',len(L),' elements')

s=1+2+3+4+5+6+7+8+9+10
print('s=',s)



########arrays#########
print('ARRAYS')
#how to define an array (warning, it should only contain numbers or arrays of numbers for the operations)
T=np.array(M) #transform a list in a array
t=np.zeros(10) #array of zeros
print('T=',T)
print('t=',t)

#operations on arrays different form operations on lists
print('M*2=',M*2)
print('T*2=',T*2)
print('T+3=',T+3)
print('T+T+T=',T+T+T)
#do you see the difference ?

#access to element is the same as list,idem for lenght
print(T[2])
print(len(t))


import matplotlib.pyplot as plt

#draw random number between [0,1]
a=np.random.random()
print('a=',a)

#draw random vector
vec=np.random.random(5,)
print('vec=',vec)

#draw a random array
t=np.random.rand(3,2)
print('t=',t)



######### functions #########

# let construct a function to compute the sum from 0 to n
def computeSum(n): #n is a input of the function
	S=0
	for i in range(n+1):
		S=S+i
	return(S) # define output with 'return'

print('ComputeSum evaluate= ',computeSum(10))


# for loop examples

S=0
for i in range(11): #Notice that is goes until 10 and not 11 !
	S=S+i
print('S=',S)

	
###########Creating Plots#############	


import matplotlib.pyplot as plt
import numpy as np
import math

#define functions and plotting functions

def f(x):
	return(-1-x+x**2)
	
x=np.linspace(-5,5,100)
f1=[math.cos(i) for i in x]
f2=f(x)


plt.figure()
plt.plot(x,f1,color='red',linestyle='-',label='function1')
plt.plot(x,f2,color='blue',linestyle='--',label='function2')
plt.title('example')
plt.xlabel('x')
plt.ylabel('function')
plt.legend()
plt.grid(True)
plt.show()


#visualize  gaussian distribution
n=10**6
gauss=np.random.normal(size=n)

plt.figure()
plt.hist(gauss, bins='auto') 
plt.show()

