from tkinter import *
from tkinter import filedialog
from random import shuffle

## Functions ##
def open_file():
    file = open(filedialog.askopenfilename())

    for line in file:
        names.append(str(line))

    Label(master,text='--------------\n'+'Original List\n'+'--------------').grid(row=2,column=0)
    for i in range(len(names)):
        Label(master,text=str(i+1)+'. '+names[i]).grid(row=i+3,column=0,sticky=W)

def randomize():
    shuffle(names)

    Label(master,text='--------------\n'+'Randomized List\n'+'--------------').grid(row=2,column=2)
    if not labels:

        for i in range (len(names)):
            l = StringVar()
            l.set(str(i+1)+'. '+names[i])
            labels.append(l)
            Label(master,textvariable=l).grid(row=i+3,column=2,sticky=W)

    else:
        for i in range (len(names)):
            labels[i].set(str(i+1)+'. '+names[i])

## Variables ##
labels = []
names = []

## GUI
master = Tk()
master.geometry('450x600')

master.title("List Randomizer")

Label(master,text='                                 ').grid(row=0,column=0)
Button(master,text='Select File',command=open_file).grid(row=0,column=1)
Button(master,text='Randomize',command=randomize).grid(row=1,column=1)

mainloop()