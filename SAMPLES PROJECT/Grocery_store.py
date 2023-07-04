print('\t\t  ************** WELCOME **************\t\t\t\n')
print('\t\t     GROCERY STORE MANAGEMENT SYSTEM')
print()
def Default_Values():
    Items_name = ['Rice      ','Suger   ','Flour    ','Oil      ','Pulses   ','Tea      ','Soft Drinks','Eggs     ','Snacks    ','Milk     ']
    Items_value = [70,80,370,1200,90,680,110,180,50,100]
    dictionary = dict(zip(Items_name,Items_value))
    d = open('Grocery Store Management.txt','w')
    for items in dictionary:
        d.write(items+"\t\t\t\t"+str(dictionary[items])+'\t\t\n')
    d.close()
    a = open('Grocery Store Management.txt','r')
    p = a.read()
    a.close()
    return p

def Total_Prize(list):
    t = sum(list)
    return t

def items_values():
    a=open('Grocery Store Management.txt','r')
    o1=a.readline()
    o2=a.readline()
    o3=a.readline()
    o4=a.readline()
    o5=a.readline()
    o6=a.readline()
    o7=a.readline()
    o8=a.readline()
    o9=a.readline()
    o10=a.readline()
    a.close()
    
    fg=o1[4:19];dd=int(fg)
    fgq=o2[5:19];d3=int(fgq)
    fg1=o3[5:19];d4=int(fg1)
    fg2=o4[5:19];d5=int(fg2)
    fg3=o5[6:19];d6=int(fg3)
    fg4=o6[5:19];d7=int(fg4)
    fg5=o7[11:19];d8=int(fg5)
    fg6=o8[5:19];d9=int(fg6)
    fg7=o9[6:19];d10=int(fg7)
    fg8=o10[5:19];d11=int(fg8)
    
    return dd,d3,d4,d5,d6,d7,d8,d9,d10,d11;
    

print('\nDear user choose one of the following option :\n')
Answer = input('1.Owner\
                2.Cashier\
                3.Customer          ')
               

try:
 if Answer =="1" :
  a=input('\nEnter Your Password:        ')
  if a=='owner':
   print('\n\t\t********** WELCOME TO YOUR STORE **********\t\t\t\ ') 
   print('Dear',"'",'Owner',"'",'You have full authority of the store')
   print()
   Choices = 'Yes' 
   while Choices == 'Yes' or Choices == 'YES' or Choices =='yes' or Choices =='yEs' or Choices =='yeS' or Choices =='YEs' or Choices =='yES' or Choices =='YeS': 
  
    print('You can Choose any number from the following Scenario.')
    print('1. Default Items and Prices Of Grocery Store.')
    print('2. List of the items with prices preseant in the store.\n3. Edit prices of the items in the store.')
    choice = input('Enter any number that you want to enter :')
    
 # ---------------------------------------------------------------------------------------------
   
    if choice=='1': 
     print('If you choose this option, All the Default Values will save in file and our old data will lost. ')
     conditial_variable=input('Do you choose it?\n\t Enter "YES" or "NO"      ')
     if conditial_variable=='YES' or conditial_variable=='yes' or Choices =='yEs' or Choices =='yeS' or Choices =='YEs' or Choices =='yES' or Choices =='YeS' or Choices =='Yes':
           print(Default_Values())
     else:
         print('OK, Your choice!')
     Choices =input('Do You Want To Resume the Calculations? \n\t\t\tpress "Yes" or "No" \n\tIf you want to quit Now,you can press "enter"   ')
    
 # -------------------------------------------------------------------------------------------
    elif choice=='2':
      try:  
       open_Variable=open('Grocery Store Management.txt','r')
       q=open_Variable.read()
       open_Variable.close()
       if q!='':
        print('List of the items in our store is as following :','\n',q,sep='')
      except FileNotFoundError:
       print('Please Set Default Values Of Grocery Store.') 
      try:
       a=open('Grocery Store Message.txt','r')
       qt=a.read()
       a.close()
       if qt!='':
        print('Dear user following items are left in our store.')
        print(qt)
      except FileNotFoundError:
          print()
      try:
       if q=='':
         print("All your Save Data is waste because of negligence of Owner.")
      except NameError:
        print()
      Choices =input('Do You Want To Resume the Calculations? \n\t\t\tpress "Yes" or "No" \n\tIf you want to quit Now,you can press "enter"   ')
 
 # ------------------------------------------------------------------------------------------- 

    elif choice=='3' :
         
     try:
      v=open('Grocery Store Management.txt','r')
      v.close()

      try:
       i=open('Grocery Store Management.txt','r')
       o=i.read()
       i.close()
      except FileNotFoundError:
       Default_Values()
      
      a=open('Grocery Store Management.txt','r')
      k=a.read()
      a.close()
      print(k)
      print('Which item\'s value you want to change?')
      c = str(input('write the name of Item:   '))
      a='Rice';b='Suger';x='Flour';d='Oil';e='Pulses'
      f='Tea';g='Soft Drinks';h='Eggs';i='Snacks';j='Milk'
      if c==a or c==b or c==x or c==d or c==e or c==f or c==g or c==h or c==i or c==j:   
         print('This Item is present in the list.')
         print('')
         print()
             
         input1_variable = int(input('Enter its old Value:     '))
         d1,d2,d3,d4,d5,d6,d7,d8,d9,d10=items_values()                                              
         list1=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
         if input1_variable in list1:
          input_variable = int(input('Enter its new Value:    '))       
          new_string=o.replace(str(input1_variable), str(input_variable))
          print('The new s','\n',new_string,sep='')
          f=open('Grocery Store Management.txt','w')
          f.write(new_string)
          f.close()
         else:
             print("Dear Owner The Old Value Of",c,"is not Exactly",input1_variable)
      else:
          print('Sorry, this item is not present in the list.')

                
     except FileNotFoundError:
      print('Please Set Default Values of Grocery Store.')
     Choices =input('Do You Want To Resume the Calculations? \
                    \n\t\t\tpress "Yes" or "No" \n\tIf you want to quit Now,you can press "enter"   ')

# -------------------------------------------------------------------------------------
    else:
        print('Please enter numbers in range of 1-3')
        Choices =input('Do You Want To Resume the Calculations? \n\t\t\tpress "Yes" or "No" \n\tIf you want to quit Now,you can press "enter"   ')
  else:      
       print('Your Password is Incorrect.') 
# ------------------------------------------------------------------------------------------
 elif Answer == "2" :
    print('\n\t\t************** WELCOME AGAIN **************\t\t\t\ ')
    w=input('Enter Your Password:         ')
    if w=='cashier':
      try:
       open_Variable=open('Grocery Store Management.txt',"r")
       q=open_Variable.read()
       open_Variable.close()
       print('Our Saved Item names and thier values selected by owner are:','\n',q,sep='')
      except FileNotFoundError:
       print('Please Set Default Values Of Grocery Store.')
      try:
       a=open('Grocery Store Message.txt','r')
       qt=a.read()
       a.close()
       if qt!='':
        print('Dear user following items left in our store.')
        print(qt)
      except FileNotFoundError:
       print()
    else:
       print('Your Password Is Incorrect.')
# ----------------------------------------------------------------------------------
 elif Answer=='3':
     print('\n\t\t********** WELCOME TO OUR STORE **********\t\t\t\ ')
     try:
      print('List of the items along with thier prices present in the store are :')
      g=open('Grocery Store Management.txt','r')
      g.close()
      try:
       open_Variable=open('Grocery Store Management.txt','r')
       q=open_Variable.read()
       open_Variable.close()
       print('','\n',q,sep='')
      except FileNotFoundError:
       print('Please Set Default Values of Grocery Store.')
      try:

       a=open('Grocery Store Message.txt','r')
       qt=a.read()
       a.close()
       if qt!='':
        print()
      except FileNotFoundError:
         print()  
      Items_names = ['Rice','Suger','Flour','Oil','Pulses','Tea','Soft Drinks','Eggs','Snacks','Milk']  
      
      try:
       l=[]
       a=int(input('Write Number of items that you want To Purchase:       '))
       q='Rice';r='Suger';s='Flour';t='Oil';u='Pulses'
       v='Tea';w='Soft Drinks';x='Eggs';y='Snacks';z='Milk'
       if a<11 and a>=0 :
        if a==0:
            print("This Means That You Don't Want To Purchase." )
        else:
         d1,d2,d3,d4,d5,d6,d7,d8,d9,d10=items_values() 
         for i in range(1,a+1):
          f =str(input('enter '+str(i)+' th'+' item name       '))
          if f.isdigit():
          	print("The Item Name Should be in Alphabetic Letters.")
          else:
           try:
#------------------------------------------------------------------------------
               
            Items_names.remove(f)
            if f==q:
               l.append(d1)
            elif f==r:
               l.append(d2)
            elif f==s:
               l.append(d3)
            elif f==t:
               l.append(d4)
            elif f==u:
                l.append(d5)
            elif f==v:
              l.append(d6)
            elif f==w:
               l.append(d7)
            elif f==x:
               l.append(d8)
            elif f==y:
               l.append(d9)    
            elif f==z:
               l.append(d10)
           except ValueError:
            print("*Try\
            \n\t\t -Enter Correct Item Name.\
                 \n\t\t -Please Don't Enter Purchased Item\'s Name.")
                     
         print("The Total Price is: ",Total_Prize(l),"/-Rs",sep='')     
#--------------------------------------------------------------------------------          
        open_Variable=open('Grocery Store Message.txt','w')
        open_Variable.write("There are "+str( len(Items_names))+" Things that Are Left In Store.\n\t")
        open_Variable.write(str(Items_names))
        open_Variable.close()  
        print('Thanks For Sopping Here.')                 
            
            
       else:
        print('There are 10 Items in Our Store!!!!')
      except ValueError:
       print('Please Write Correct Name of Item.\
             \n Or If You Repeat Any Item\'s Name, You Will Not Able To Purchase.') 
     except FileNotFoundError:
      print('Please Connect to Owner of Grocery Store.')
      print('Because We Have No Any Item Available for Purches.')

# ------------------------------------------------------------------------------------------

 else:
    print('There are Options in the range of 1-3. ')
except ValueError:
    print('Please Enter Required Input.')