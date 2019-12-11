'''
Leeds 2019
Animation of simple SIR model.
Plots of S vs I, S vs time and I vs time.
'''
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib
import numpy as np

N = 1000
y0 = 10
t,x0 = 0,N-y0
a = 1.0
r = a/(0.4*N)
dt = 0.1
tmax = 20
steps = np.linspace(0,tmax,int(tmax/dt)+1)

odefig,(ax1,ax2) = plt.subplots(figsize=(8,8),nrows=2)
params = {'font.family': 'serif'}
matplotlib.rcParams.update(params)

ts,xs,ys = [0],[x0],[y0]
mysi, = ax1.plot(xs,ys,'r')
myx, = ax2.plot(ts,xs,'g',label='$S$')
myy, = ax2.plot(ts,ys,'r',label='$I$')

mystr = '$r=$'+str(r)[:6]+'\n$a=$'+str(a)+'\n$N=$'+str(N)+'\n$I(0)=$'+str(int(y0))

ode1 = '$\\frac{dS}{dt}=-r S I$'
ode2 = '$\\frac{dI}{dt}= r S I - aI$'

def init():
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.plot([0,N],[N,0],'k:')
    ax1.plot([a/r,a/r],[0,N-a/r],'k:')
    ax1.text(N*.8,N*.8,mystr)
    ax1.text(N*.4,N*.92,ode1)
    ax1.text(N*.4,N*.84,ode2)
    ax1.set_xticks([N/5,2*N/5,3*N/5,4*N/5,N])
    ax1.set_xlim([0,N*1.01])
    ax1.set_ylim([0,N*1.02])
    ax1.set_xlabel('$S$')
    ax1.set_ylabel('$I$')
    ax1.set_title('SIR',fontsize=20)
    mysi.set_data(xs,ys)
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    ax2.set_xlabel('$t$')
    ax2.set_xlim([0,tmax])
    ax2.set_ylim([0,N*1.02])
    ax2.set_xticks([tmax/2,tmax])
    ax2.legend()
    myx.set_data(ts,xs)
    myy.set_data(ts,ys)
    return mysi,myx,myy

def euler(x,f,h):
    ''' the euler method is x(t+dt) = x(t) + dt*f(x(t)).
        this function returns x(t+dt) given x(t), f and dt'''
    return x+f(x)*h

def RK2(x,f,h):
    ''' the RK2 method. returns x(t+dt) given x(t), f and dt'''
    K1 = h*f(x)
    K2 = h*f(x+K1)
    return x+0.5*(K1+K2)

def twoodes(twovars):
    ''' twovars is [x,y] '''
    x,y = twovars[0],twovars[1]
    dxdt = -r*x*y
    dydt = r*x*y - a*y
    return np.array([dxdt,dydt])

def animateode(step):
    ''' solve ODEs in steps of duration dt'''
    myvariables = np.array([xs[-1],ys[-1]])
    x,y = RK2(myvariables,twoodes,dt)
    ts.append(step)
    xs.append(x)
    ys.append(y)
    mysi.set_data(xs,ys)
    ax1.set_title('SIR',fontsize=20)
    myx.set_data(ts,xs)
    myy.set_data(ts,ys)
    return mysi,myx,myy,

odesim = anim.FuncAnimation(odefig,animateode,frames=steps,
                            init_func=init,interval=1,
                            repeat=False)

plt.savefig('SIR.pdf')
plt.show()

