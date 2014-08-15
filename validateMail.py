email = raw_input("Enter sample Mail")

sep_at = email.split('@')
sep_dot = sep_at[1].split('.')
if(sep_at[0]==""): 
       print 'Wrong Mail ID',email
                    
elif(len(sep_at)==1):
	print 'Wrong Mail ID',email
                        
elif(sep_dot[0]==""): 
        print 'Wrong Mail ID',email
                
elif(len(sep_dot)==1):
        print 'Wrong Mail ID',email

elif(len(sep_dot)>1):
	if(sep_dot[1]==""):
	        print 'Wrong Mail ID',email
else:
    print 'Correct Id'


