from Tkinter import *

from re import *

from urllib import *

from time import *

from tkMessageBox import *

import os

mails = []

all_links = []

def status():
    for i in stateList:
        print i

def scrapMail(url,depth):
    counter = 0
    flag = 0
    if(depth==0):
        return
    else:
        try:
            source = urlopen(url).read()
            for k in all_links:
                if(k==url):
                    flag=1
                    break
            if(not (flag)):
                all_links.append(url)
            else:
                flag=0
                return
        except Exception as e:
            print '--------------'
            print 'UNABLE TO LOAD PAGE ',url
            print '--------------'
            return
        hyperLink = findall('<a href="(.*?)"',source)
        for link in hyperLink:
            if(search(r'http[s]?://.*',link)==None):
                link = url + link
                #link = url +'/'+ link
            print 'Processing--->',link
            scrapMail(link,depth-1)
    return            


def submitWebsite():
    all_mails=[]
    url = website.get()#"http://www."+website.get()
    #source=urlopen(url).read()
    #findMail(url,3)
    scrapMail(url,2)
    counter=0
    print all_links
    for link in all_links:
        try:
             src = urlopen(link).read()
        except Exception as e:
            print '--------------'
            print 'UNABLE TO LOAD PAGE ',link
            print '--------------'
            continue
        print 'Processing --> ',link
        mails = findall(r'([A-Za-z0-9_\-\.]*?@[A-Za-z0-9\._\-]*)',src)
        print "Mails --> ",mails
        for now in mails:
            counter=0
            print 'now at start --> ',now
            print 'all_mails --> ',len(all_mails)
            if(len(all_mails)==0):
                print 'Working on length 0'
                sep_at = now.split('@')
                sep_dot = sep_at[1].split('.')
                if(sep_at[0]==""):
                    print 'Wrong Mail ID',now
                
                elif(len(sep_at)==1):
                    print 'Wrong Mail ID',now
                    
                elif(sep_dot[0]==""): 
                    print 'Wrong Mail ID',now
                    
                elif(len(sep_dot)==1):
                    print 'Wrong Mail ID',now

                elif(len(sep_dot)>1):
                    if(sep_dot[1]==""):
                        print 'Wrong Mail ID',now

                    else:
                        print "Adding --> ",now
                        all_mails.append(now)
            else:        
                for already in all_mails:
                    if(now==already):
                        print "Equal Condition Statisfied"
                        counter = 1
                        break
                if(counter == 0):
                    sep_at = now.split('@')
                    sep_dot = sep_at[1].split('.')
                    if(sep_at[0]==""):
                        print 'Wrong Mail ID',now
                    
                    elif(len(sep_at)==1):
                        print 'Wrong Mail ID',now
                        
                    elif(sep_dot[0]==""): 
                        print 'Wrong Mail ID',now
                        
                    elif(len(sep_dot)==1):
                        print 'Wrong Mail ID',now

                    elif(len(sep_dot)>1):
                        if(sep_dot[1]==""):
                            print 'Wrong Mail ID',now
                        else:
                            print "Adding --> ",now
                            all_mails.append(now)
                    else:
                        print "Adding --> ",now
                        all_mails.append(now)
                else:
                    counter = 0
            print '---------------------------'
            print '           ALL_MAILS       '
            print '---------------------------'
            for i in all_mails:
                print i
            counter =0

            
    fp = open('mailList.txt','w')
    for i in all_mails:
        print "Writing --> ",i
        fp.write(str(i))
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
        

def menu():
    root.geometry('500x500')
    Label(root,text='Enter Website',font=('A',15)).place(x=70,y=150)
    Entry(root,textvariable=website).place(x=70,y=190)
    Button(root,text='OK',command=submitWebsite).place(x=250,y=183)
    return

all_links = []

root = Tk()

stateList = []

website = StringVar()

root.geometry('500x500')

menu()

root.mainloop()
