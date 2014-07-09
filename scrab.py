from Tkinter import *

from re import *

from urllib import *

from time import *

from tkMessageBox import *

import os

def status():
    for i in stateList:
        print i

def submitWebsite():
    url = "http://www."+website.get()
    source = urlopen(url).read()
    mail = findall(r'([A-Za-z0-9_\-\.]*?@[A-Za-z0-9\._\-]*)',source)
    fp = open('mailList.txt','w')#mailList.txt
    for i in mail:
        stateList.append(Checkbutton(text=i).pack())
        fp.write(i)
        fp.write('\n')
    fp.close()
    Label(root,text='File Saved Successfuly').place(x=100,y=220)
    sleep(3)
    ans = askyesno('MailList.txt','Do You Want to Open A File')
    print ans
    if(ans):
        path = "xdg-open "+os.getcwd()+"/mailList.txt"
        os.system(path)
        Label(root,text='File Saved Successfuly',fg='lightgrey',bg='lightgrey').place(x=100,y=220)    

    Button(text='Get Status',command=status).place(x=200,y=200)
    return
    
def menu():
    root.geometry('500x500')
    Label(root,text='Enter Website',font=('A',15)).place(x=70,y=150)
    Entry(root,textvariable=website).place(x=70,y=190)
    Button(root,text='OK',command=submitWebsite).place(x=250,y=183)
    return

root = Tk()

stateList = []

website = StringVar()

root.geometry('500x500')

menu()

root.mainloop()
