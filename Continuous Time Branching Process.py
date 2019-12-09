from tkinter import *
import sys,copy,tkinter.messagebox
from numpy import *

tree=Tk()
tree.title('continuous-time branching process')
top=Frame(tree)
top.pack(side=TOP)

bframe=Frame(tree)
bframe.pack(side=LEFT)

class bcanvas: 
    def __init__(self,root,width,height):
        self.root=root
        self.width=width
        self.height=height
        try:
           self.canvas = Canvas(self.root, width=self.width, height=self.height, bg = 'white')
           self.canvas.pack()
           self.clear()
        except:
           print ('An error has occured in init!')

    def clear(self):
        try:
           self.canvas.create_rectangle(0,0,self.width,self.height,fill='white')
        except:
           print ('An error has occured in clear!')

    def drawb(self,t,y):  
        r=0.015*self.height
        self.canvas.create_oval(self.width*t-r,self.height*y-r,self.width*t+r,self.height*y+r,outline='black', fill='blue')

    def drawd(self,t,y):  
        r=0.015*self.height
        self.canvas.create_oval(self.width*t-r,self.height*y-r,self.width*t+r,self.height*y+r,outline='black', fill='red')


    def drawl(self,x,dx,v):
        for y in v:
            self.canvas.create_line((self.width*x,self.height*y),(self.width*x+self.width*dx,self.height*y),width=2,fill='blue')

    def drawv(self,t,y1,y2):
        self.canvas.create_line((self.width*t,self.height*y1),(self.width*t,self.height*y2),width=2,fill='blue')

onoff=False
def toggle(event):
   global onoff
   if onoff:
      onoff=False
   else:
      onoff=True

b=0.2
d=0.1
tmax=15.0
dt=tmax/1000.0

# Runs the animation when button is pressed
def run():
   global onoff 
   tmax=tm.get()
   b=pbor.get()
   d=pdie.get()
   error=StringVar()     

   n=n1.get()#int(input)
   print ('===start run===')
   cg.clear()

   v=[] # list of living individuals; stores a vertical position for each
   if n==1:v=[0.5]  # start with one
   if n==2:v=[0.3,0.6]
   if n==3:v=[0.25,0.5,0.75]
   if n==4:v=[0.2,0.4,0.6,0.8]

   t=0
   while t<=tmax and len(v)>0:
      t+=dt
      rate = b*len(v)
      urv=random.random()
      if urv < rate*dt:
         print (urv,b*len(v),d*len(v))
         if len(v)==1:
            vnow=sum(v)
            v=[0.5*vnow,0.5*(1+vnow)]
            print (v)
            cg.drawb(t/tmax,v[0])
            cg.drawb(t/tmax,v[1])
            cg.drawv(t/tmax,v[0],v[1])
         else:
            i=random.randint(len(v))
            vm1=v[i]
            if i==0:
               newv=(0.05+vm1)/2
            else:
               vm2=v[i-1]
               newv=vm1+(vm2-vm1)/3.0
            v[i]=newv
            if i==len(v)-1:
               pairv=(0.95+vm1)/2
            else:
               vm2=v[i+1]
               pairv=vm1+(vm2-vm1)/3.0
            v.append(pairv)
            cg.drawv(t/tmax,newv,pairv)
            cg.drawb(t/tmax,newv)
            cg.drawb(t/tmax,pairv)
            v.sort()
         print (t,len(v))
      else:
         rate = (b+d)*len(v)
         if urv<rate*dt:
            print ('death')
            i=random.randint(len(v))
            cg.drawd(t/tmax,v[i])
            v.pop(i)

      cg.drawl(t/tmax,dt/tmax,v)
      tree.update()
      tree.after(5)
      if sum(v)==0:
         tkinter.messagebox.Message(icon='info',type='ok',message='Population went extinct',title='Results').show()
         t=tmax

   print ('finished')

but=Button(top, text='Start/Stop',command=run)
but.bind('<Button-1>',toggle)
but.pack(side=TOP)
tm=Scale(top, orient=HORIZONTAL, length=184, from_=0.0, to=20.0, tickinterval=5, resolution=5,label='maximum time')
tm.set(tmax)
tm.pack(side=LEFT)

# Now the sliders (in a frame called sframe)
pbor=Scale(top, orient=HORIZONTAL, length=214, from_=0., to=1.2, tickinterval=.5, resolution=0.1,label='birth')
pbor.set(b)
pbor.pack(side=LEFT)
pdie=Scale(top, orient=HORIZONTAL, length=214, from_=0., to=1.2, tickinterval=.5, resolution=0.1,label='death')
pdie.set(d)
pdie.pack(side=LEFT)

n1=Scale(top, orient=HORIZONTAL, length=184, from_=0, to=4, tickinterval=1, resolution=1,label='Starting number of cells')
n1.set(1)
n1.pack(side=LEFT)

totalwidth=1200
totalheight=300
cg=bcanvas(tree,totalwidth,totalheight)

tree.mainloop()
