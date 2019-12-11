import pylab as pl

def f(x):
    ''' a function of one variable '''
    return x*(1-x)


# now solve a ODE with one variable using Euler method
x0 = 0.5
dt = 0.01
x = x0
t = 0
print(x)
while t<1:
   x = x + f(x)*dt
   t = t + dt
#   print(t,x)
   
def gandh(y,z):
    ''' two functions of two variables '''
    r = 1.0
    k = 2.0
    dydt = r*y -k*z
    dzdt = r*z - k*y*z
    return dydt,dzdt

# now solve a pair of ODEs for two variables using Euler method
y0,z0 = 1,2  # initial conditions
t = 0
tlist,ylist,zlist = [],[],[]
y=y0
z=z0
print(t,y,z)
while t < 0.3:
   dydt,dzdt = gandh(y,z)
   y = y + dydt*dt
   z = z + dzdt*dt
   t = t + dt
   ylist.append(y)
   zlist.append(z)
   tlist.append(t)
print(ylist)

# make plots. y vs t and z vs y
pl.subplot(211)
pl.plot(tlist,ylist)
pl.xlabel('$t$')
pl.ylabel('$y$')
pl.subplot(212)
pl.plot(ylist,zlist)
#pl.ylabel('$z$')    
pl.ylabel('$z$')
pl.xlabel('$y$')

pl.tight_layout()   
pl.show()
