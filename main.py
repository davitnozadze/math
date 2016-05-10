from tkinter import *
from math import *
import turtle
mashtab=50
#function for calculation
a =0
b = 0
c = 0
z=0
f=0
Ka = 0
Kb = 0
Kc = 0
i=0
j=0
def calculation():
    global a,b,c, Ka,Kb,Kc,r,R
    Lb1.delete(0,"end")
    if var.get()=="სამკუთხედი":
        a=float(E3.get())
        b=float(E2.get())
        c=float(E1.get())
        if a+b>c and a+c>b and c+b>a:
            label.config(text = "თქვენ აირჩიეთ : სამკუთხედი",fg="blue")
            p=(a+b+c)/2
            s=(p*(p-a)*(p-b)*(p-c))**0.5
            sina=((2*s)/(b*c))
            sinb=((2*s)/(a*c))
            sinc=((2*s)/(a*b))
            Ka=(degrees(asin(sina)))
            Kb=(degrees(asin(sinb)))
            Kc=(degrees(asin(sinc)))
            if Ka+Kb+Kc<179:
            	mas=[Ka,Kb,Kc]
            	max_index=(mas.index(max(mas)))
            	if max_index==0:
            		Ka=180-Ka
            	elif max_index==1:
            		Kb=180-Kb
            	elif max_index==2:
            		Kc=180-Kc

            cosa=round(sqrt(1-sina**2), 4)
            cosb=round(sqrt(1-sinb**2), 4)
            cosc=round(sqrt(1-sinc**2), 4)
            Ha=round((2*s)/a, 2)
            Hb=round((2*s)/b, 2)
            Hc=round((2*s)/c, 2)
            Ma=round(0.5*sqrt(2*(b**2+c**2)-a**2), 3)
            Mb=round(0.5*sqrt(2*(a**2+c**2)-b**2), 3)
            Mc=round(0.5*sqrt(2*(b**2+a**2)-c**2), 3)
            La=round(sqrt(c*b*(a+b+c)*(b+c-a))/(b+c), 3)
            Lb=round(sqrt(a*c*(a+b+c)*(a+c-b))/(a+c), 3)
            Lc=round(sqrt(a*b*(a+b+c)*(a+b-c))/(a+b), 3)
            R=round((a*b*c)/(4*s), 3)
            r=s/p
            
            Lb1.insert(1," ფართობი : {}".format(round(s,2)))
            Lb1.insert(2," პერიმეტრი : {}".format(round(2*p,2)))
            Lb1.insert(3," ∠a : {}".format(round(Ka,3)))
            Lb1.insert(4," ∠b : {}".format(round(Kb,3)))
            Lb1.insert(5," ∠c : {}".format(round(Kc,3)))
            Lb1.insert(6," SIN(∠a) : {}".format(round(sina,4)))
            Lb1.insert(7," SIN(∠b) : {}".format(round(sinb,4)))
            Lb1.insert(8," SIN(∠c) : {}".format(round(sinc,4)))
            Lb1.insert(9," COS(∠a) : {}".format(cosa))
            Lb1.insert(10," COS(∠b) : {}".format(cosb))
            Lb1.insert(11," COS(∠c) : {}".format(cosc))
            Lb1.insert(12," H(A) : {}".format(Ha))
            Lb1.insert(13," H(B) : {}".format(Hb))
            Lb1.insert(14," H(C) : {}".format(Hc))
            Lb1.insert(15," M(a) : {}".format(Ma))
            Lb1.insert(16," M(b) : {}".format(Mb))
            Lb1.insert(17," M(c) : {}".format(Mc))
            Lb1.insert(18," L(A) : {}".format(La))
            Lb1.insert(19," L(B) : {}".format(Lb))
            Lb1.insert(20," L(C) : {}".format(Lc))
            Lb1.insert(21," R : {}".format(R))
            Lb1.insert(22," r : {}".format(round(r,2)))
            
        else : 
            label.config(text = "თქვენ არღვევთ სამკუთხედის უტოლობის წესს :)",fg="red")
            # L4.config(text="პერიმეტრი : ")
            # L5.config(text="ფართობი : ")

    elif var.get()=="მართკუთხედი":
        a=float(E3.get())
        b=float(E2.get())
        p=2*(a+b)
        s=a*b
        d=sqrt(a**2+b**2)
        R=d/2
        r=a/2
        
        Lb1.insert(1," ფართობი : {}".format(round(s,4)))
        Lb1.insert(2," პერიმეტრი : {}".format(round(p,4)))
        Lb1.insert(4," R : {}".format(round(R,4)))
        if a==b:

        	Lb1.insert(3," r : {}".format(round(r,4)))
        else:
        	Lb1.insert(3," წრეწირი არ ჩაიხაზება !!!")
        	Ch1.config(state=DISABLED,text="წრეწირი არ ჩაიხაზება")
        #L4.config(text="პერიმეტრი : {}".format(p))
    elif var.get()=="წრეწირი":
        
        r=float(E3.get())
        p=2*pi*r
        s=(r**2)*pi
        p = round(p, 4)
        s = round(s, 4)

        
        Lb1.insert(1," ფართობი : {}".format(s))
        Lb1.insert(2," პერიმეტრი : {}".format(p))
        
        #L5.config(text="ფართობი : {}".format(s))
        #L4.config(text="პერიმეტრი : {}".format(p))

#defines selected figure
def sel():
    selection = "თქვენ აირჩიეთ : " + var.get()
    label.config(text = selection,fg="blue")
    pen.clear()
    pen.reset()
    #L5.config(text="ფართობი : ")
    if var.get()=="მართკუთხედი":
        E1.delete(0, 'end')
        E2.delete(0, 'end')
        E3.delete(0, 'end')
        E1.config(state=DISABLED,cursor="trek",bd=0)
        E2.config(state=NORMAL,cursor='xterm',bd=4)
        E3.config(state=NORMAL,cursor="xterm",bd=4)
        Ch1.config(state=NORMAL,text="ჩაიხაზოს წრეწირი")
        Ch2.config(state=NORMAL)
        L3.config(text="a :")
        L1.config(text="         ")
        L2.config(text="  b : ")
        
        Lb1.delete(0,"end")
        
    elif var.get()=="სამკუთხედი":
        E1.delete(0, 'end')
        E2.delete(0, 'end')
        E3.delete(0, 'end')
        E1.config(state=NORMAL,cursor="xterm",bd=4)
        E2.config(state=NORMAL,cursor="xterm",bd=4)
        E3.config(state=NORMAL,cursor="xterm",bd=4)
        Ch1.config(state=NORMAL,text="ჩაიხაზოს წრეწირი")
        Ch2.config(state=NORMAL)
        L3.config(text="a :")
        L2.config(text="  b : ")
        L1.config(text="  c : ")
        
        Lb1.delete(0,"end")
        
    elif var.get()=="წრეწირი":
        E1.delete(0, 'end')
        E2.delete(0, 'end')
        E3.delete(0, 'end')
        E1.config(state=DISABLED,cursor='trek',bd=0)
        E2.config(state=DISABLED,cursor='trek',bd=0)
        E3.config(state=NORMAL,cursor="xterm",bd=4) 
        Ch1.config(state=DISABLED)
        Ch2.config(state=DISABLED)
        
        L3.config(text="r :")
        L1.config(text="         ")
        L2.config(text="         ")

        Lb1.delete(0,"end")
# mashtab function for drawing triangular
def mashtab_t(x, y,z):
    k = max(x,y,z)
    m = 50
    if k%6==0:
        k= k/6
        return m/k
    else:
        k = int(k/6)+1
        return m/k
# mashtab for rectangular
def mashtab_r(x, y):
    k = max(x,y)
    m = 50
    if k%6==0:
        k= k/6
        return m/k
    else:
        k = int(k/6)+1
        return m/k

#mashtab function for circle
def mashtab_c(k):
    m = 25
    if k%6==0:
        k= k/6
        return m/k
    else:
        k = int(k/6)+1
        return m/k
#about_menu function        
def about_window():
    root1 = Tk()
    root1.geometry ("400x500")
    root1.title("About")
    text = Text(root1)
    text.insert(INSERT, "I am a program \n")
    text.insert(INSERT, "aq chawere rac ginda rom eweros \nsheni programis shesaxeb")
    text.config(state=DISABLED)
    text.pack()
    root1.mainloop()
#drawing function
def draw_r(x,y):
	global Ka,r,Kb,f
	f=1
	if var.get()=="სამკუთხედი":
		k1=tan(radians(Ka/2))
		B1=y-k1*x
		k2=-tan(radians(Kb/2))
		B2=y-k2*(x+mashtab*c)
		X=(B1-B2)/(k2-k1)
		Y=k2*X+B2
		pen.up()
		pen.goto(X,y)
		pen.pd()
		pen.circle(r*mashtab)
		pen.up()
	if var.get()=="მართკუთხედი":
		if E2.get()==E3.get():
			pen.goto(x+(float(E2.get())*mashtab/2),y)
			pen.pd()
			pen.circle(r*mashtab)
			pen.up()

def draw_R (x,y):
	global Kc,R,z,a,b
	z=1
	if var.get()=="სამკუთხედი":
		pen.goto(x,y)
		pen.rt(Kc)
		pen.pd()
		pen.circle(R*mashtab)
		pen.lt(Kc)
		pen.up()
	if var.get()=="მართკუთხედი":
		pen.goto(x,y)
		pen.pd()
		kutxe=degrees(atan(a/b))
		pen.rt(kutxe)
		pen.circle(R*mashtab)
		pen.lt(kutxe)
		pen.up()
def draw():
    calculation()
    pen.clear()
    pen.reset()
    global mashtab,r,Ka,Kc,R,i,j,x,y,z,f
    z=0
    f=0
    Ch1.config(state=NORMAL,text="ჩაიხაზოს წრეწირი")
    if var.get()=="სამკუთხედი" and a+b>c and a+c>b and c+b>a:
        mashtab = mashtab_t(a,b,c)
        pen.up()
        if Ka>90:
        	pen.goto(-30,-150)
        	x=-30
        	y=-150
        else:
        	pen.goto(-150, -100)
        	x=-150
        	y=-100
        pen.pd()
        pen.fd(mashtab*c)
        pen.lt(180-Kb)
        pen.fd(mashtab*a)
        pen.lt(180-Kc)
        pen.fd(mashtab*b)
        pen.lt(180-Ka)
        if i==1:
        	draw_r(x,y)
        
        #shemoxazuli
        if j==1:
        	draw_R(x,y)
        	

    elif var.get()=="მართკუთხედი":
        mashtab = mashtab_r(a,b)
        pen.up()
        pen.goto(-150, -150)
        x=-150
        y=-150
        pen.pd()
        pen.fd(mashtab*a)
        pen.lt(90)
        pen.fd(mashtab*b)
        pen.lt(90)
        pen.fd(mashtab*a)
        pen.lt(90)
        pen.fd(mashtab*b)
        pen.lt(90)
        pen.up()
        if i==1:
        	draw_r(x,y)
        if j==1:
        	draw_R(x,y)
        if a!=b:
        	Ch1.config(state=DISABLED,text="წრეწირი არ ჩაიხაზება")
    elif var.get()=="წრეწირი":
        r=float(E3.get())
        mashtab = mashtab_c(r)
        pen.up()
        pen.goto(0, -150)
        pen.pd()
        pen.circle(r*mashtab)
    canvas.itemconfig(scale,text="scale : 1 : {}".format(round(50/mashtab,0)))

def Checkcommand():
	global i,x,y,f
	i=CheckVar1.get()
	if CheckVar1.get()==1:
		if f==0:
			draw_r(x,y)
			f+=1
	

def Checkcommand1():
	global j,x,y,z
	j=CheckVar2.get()
	if CheckVar2.get()==1:
		if z==0:
			draw_R(x,y)
			z+=1



root = Tk()
root.geometry("850x580")
root.withdraw()

var = StringVar()
# radiobutton frame
frame=Frame(root).grid(rowspan=24,columnspan=24)

image_sam=PhotoImage(file="samkutxedi_ax.png")
image_otx=PhotoImage(file="otxkutxedi_ax.png")
image_wre=PhotoImage(file="wre_ax.png")
label = Label(frame, text="აირჩიეთ ფიგურა ",font="Arial=10",fg="blue")
label.grid(row=0,column=5,columnspan=10)
# top=Frame(root).grid(rowspan=5, columnspan=10)

#labels and entrys
L1 = Label(frame, text=" c :",font="Arial 15")
E1 = Entry(frame, bd =4,width=6,state=DISABLED)#,cursor="trek")

L2 = Label(frame, text=" b :",font="Arial 15")
E2 = Entry(frame, bd =4,width=6,state=DISABLED)

L3 = Label(frame, text=" a :",font="Arial 15")
E3 = Entry(frame, bd =4,width=6,state=DISABLED)

# L4 = Label(frame, text="პერიმეტრი : ",font="Arial 15")
# L5 = Label(frame, text="ფართობი : ",font="Arial 15")

#calculating button
but=Button(frame,text="Calculation",command=calculation)
draw_but = Button(frame, text = "Draw", command=draw)
#griding them
L1.grid(row=4,column=19)
E1.grid(row=4,column=20)

L2.grid(row=4,column=17)
E2.grid(row=4,column=18)

L3.grid(row=4,column=15)
E3.grid(row=4,column=16)
# end of gridding
# gridding answers list   ##################################################################
# L4.grid(row=21,columnspan=2)
# L5.grid(row=22, columnspan=2)

scrollbar = Scrollbar(frame, width= 16) 
scrollbar.grid(row= 8, column=8 ,sticky = N+S)
Lb1 = Listbox(frame,bg="#D8D8D8",font="Arial 15",yscrollcommand=scrollbar.set) 
Lb1.grid(row = 8, column=7)#,sticky = N+S)

scrollbar.config(command=Lb1.yview)

##################################################################################################




but.grid(row = 5, column=7, padx = 7)
draw_but.grid(row = 12, column = 18)
#################################################

canvas = Canvas(frame, width=350, height=350)
canvas.grid(row=5,rowspan=7, column =13 ,columnspan=16,padx=10)#, sticky=W+E+N+S)
pen = turtle.RawTurtle(canvas)
scale=canvas.create_text(0,-140,text="scale >> 1 : {} ".format(50/mashtab),font="Arial=5")
# turtle2 = turtle.RawTurtle(canvas)


root.deiconify()




##################################################################
R1 = Radiobutton(frame, text="სამკუთხედი", variable=var, value="სამკუთხედი",image=image_sam,compound="left",command=sel)
R1.grid(row=1,rowspan=6,column=1,columnspan=4)

R2 = Radiobutton(frame, text="მართკუთხედი", variable=var, value="მართკუთხედი",image=image_otx,compound="left",command=sel)
R2.grid(row=6,rowspan=4,columnspan=5)

R3 = Radiobutton(frame, text="წრეწირი", variable=var, value="წრეწირი",image=image_wre,compound="left",command=sel)
R3.grid(row=10,rowspan=4,columnspan=4)
#####################################################################
CheckVar1=IntVar()
CheckVar2=IntVar()
Ch1=Checkbutton(frame,text="ჩაიხაზოს წრეწირი",justify="left",variable=CheckVar1,onvalue=1,offvalue=0,command=Checkcommand)
Ch1.grid(row=12,column=14,columnspan=4)
Ch2=Checkbutton(frame,text="შემოიხაზოს წრეწირი",justify="right",variable=CheckVar2,onvalue=1,offvalue=0,command=Checkcommand1)
Ch2.grid(row=13,column=14,columnspan=4)

# menus #start*#
main_menu = Menu(root)
root.config(menu = main_menu)

help_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(menu = help_menu, label = "Help")

help_menu.add_cascade(label = "About", command = about_window)
#menus end




root.mainloop()

