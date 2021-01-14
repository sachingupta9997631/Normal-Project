from tkinter import *

win=Tk()
win.geometry("500x620+500+100")
win.title("Calculator (By: Sachin Gupta)")
win.config(bg="white")

heading = Label(win,text="Calculator",font=("bahnschrift semibold",32),bg="white",fg="RED")
heading.pack()

frameup=Frame(win,bg="lightgreen")
frameup.pack(side=TOP)

framedown = Frame(win,bg="Lightblue")
framedown.pack(side=BOTTOM)

##############################Functions defined###########################

def clear():
    global val
    in_box.delete(0,"end")
    out_box.delete(0,"end")
    val=" "


def backsp():
    global val
    temp=cal.get()
    temp=temp[0:-1]
    val=temp
    cal.set(temp)


def check():
    global out
    a=cal.get()
    a=str(a)
    calc=eval(a)
    out.set(calc)

#######################################################################

val=" " #global variable for storing the values together
cal=StringVar()
out=StringVar()

def values(operator):
    global val
    val=val+str(operator)
    cal.set(val)

text1=Label(frameup,text="INPUT BOX",font=("bahnschrift semibold",15),fg="green",bg="lightgreen")
text1.pack(pady=5)

in_box=Entry(frameup,font=("bahnschrift semibold",18),textvariable=cal,bg="white",fg="lightgreen")
in_box.pack(pady=10, padx=20)

text2=Label(frameup,text="OUTPUT BOX",font=("bahnschrift semibold",15),fg="green",bg="lightgreen")
text2.pack(pady=5)

out_box=Entry(frameup,font=("bahnschrift semibold",18), textvariable=out ,fg="lightgreen",bg="white")
out_box.pack(pady=10)


######################creation of the Buttons##############################
but1=Button(framedown,text=" 1 ",font=("consolas",18),bg="white",fg="black",command=lambda: values(1))
but1.grid(row=0,column=0,pady=10,padx=10)

but2=Button(framedown,text=" 2 ",font=("consolas",18),bg="white",fg="black",command=lambda: values(2))
but2.grid(row=0,column=1,pady=10,padx=10)

but3=Button(framedown,text=" 3 ",font=("consolas",18),bg="white",fg="black",command=lambda: values(3))
but3.grid(row=0,column=2,pady=10,padx=10)

but4=Button(framedown,text=" 4 ",font=("consolas",18),bg="white",fg="black",command=lambda: values(4))
but4.grid(row=1,column=0,pady=10,padx=10)

but5=Button(framedown,text=" 5 ",font=("consolas",18),bg="white",fg="black",command=lambda: values(5))
but5.grid(row=1,column=1,pady=10,padx=10)

but6=Button(framedown,text=" 6 ",font=("consolas",18),bg="white",fg="black",command=lambda: values(6))
but6.grid(row=1,column=2,pady=10,padx=10)

but7=Button(framedown,text=" 7 ",font=("consolas",18),bg="white",fg="black",command=lambda: values(7))
but7.grid(row=2,column=0,pady=10,padx=10)

but8=Button(framedown,text=" 8 ",font=("consolas",18),bg="white",fg="black",command=lambda: values(8))
but8.grid(row=2,column=1,pady=10,padx=10)

but9=Button(framedown,text=" 9 ",font=("consolas",18),bg="white",fg="black",command=lambda: values(9))
but9.grid(row=2,column=2,pady=10,padx=10)

add=Button(framedown,text=" + ",font=("consolas",18),bg="white",fg="black",command=lambda: values('+'))
add.grid(row=0,column=3,pady=10,padx=10)

dif=Button(framedown,text=" - ",font=("consolas",18),bg="white",fg="black",command=lambda: values('-'))
dif.grid(row=1,column=3,pady=10,padx=10)

mul=Button(framedown,text=" * ",font=("consolas",18),bg="white",fg="black",command=lambda: values('*'))
mul.grid(row=2,column=3,pady=10,padx=10)

div=Button(framedown,text=" / ",font=("consolas",18),bg="white",fg="black",command=lambda: values('/'))
div.grid(row=3,column=3,pady=10,padx=10)

zero=Button(framedown,text=" 0 ",font=("consolas",18),bg="white",fg="black",command=lambda: values(0))
zero.grid(row=3,column=1,pady=10,padx=10)

dot=Button(framedown,text=" . ",font=("consolas",18),bg="white",fg="black",command=lambda: values('.'))
dot.grid(row=3,column=0,pady=10,padx=10)

mod=Button(framedown,text=" % ",font=("consolas",18),bg="white",fg="black",command=lambda: values('%'))
mod.grid(row=3,column=2,pady=10,padx=10)

equal=Button(framedown,text=" = ",font=("consolas",18),bg="white",fg="black",command=check)
equal.grid(row=4,column=3,pady=10,padx=10)

clr=Button(framedown,text=" C ",font=("consolas",18),bg="white",fg="black",command=clear)
clr.grid(row=4,column=1,pady=10,padx=10)

popone=Button(framedown,text=" <- ",font=("consolas",16),bg="white",fg="black",command=backsp)
popone.grid(row=4,column=0,pady=10,padx=10)

win.mainloop()
