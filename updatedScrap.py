from re import *
from urllib import *

def scrapMail(url,depth):
    counter = 0
    if(depth==0):
        return
    else:
        source = urlopen(url).read()
        hyperLink = findall('<a href="(.*?)"',source)
        for link in hyperLink:
            if(search(r'http[s]?://.*',link)==None):
                link = url + link
                #link = url +'/'+ link
            print 'Processing--->',link
            src = urlopen(link).read()
            mails = findall(r'([A-Za-z0-9_\-\.]*?@[A-Za-z0-9\._\-]*)',src)    
            for now in mails:
                for already in all_mails:
                    if(now==already):
                        counter = 1
                        break
                if(counter == 0):
                    sep_at = now.split('@')
                    sep_dot = sep_at[1].split('.')
                    if(sep_at[0]==""):
                        print 'Wrong Mail ID',now
                    
                    elif(len(sep_at)==1):
                        print 'Wrong Mail ID',now
                        
                    elif(sep_dot[0]=="" or sep_dot[1]==""):
                        print 'Wrong Mail ID',now
                        
                    elif(len(sep_dot)==1):
                        print 'Wrong Mail ID',now
                        
                    else:
                        print now
                        all_mails.append(now)
                else:
                    counter = 0
            for i in all_mails:
                print i
                print '-----'   
            scrapMail(link,depth-1)
    return            


all_mails = []

