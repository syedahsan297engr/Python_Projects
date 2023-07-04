

#IMPORTING LIBRARIES
from pygame import mixer #Song play,pause,anything
import tkinter as tk #for GUI                                      #INSTALL THIS LIBRARY tkinter
from tkinter import * #For labels and buttons
from tkinter.filedialog import askopenfilename #to select file
import random #to use random numbers
from PIL import ImageTk,Image                                       #INSTALL LIBRARY PILLOW
from time import sleep
from tkinter import messagebox 
import mutagen                                                      #INSTALL THIS LIBRARY mutagen
from mutagen.mp3 import MP3
import sys
sys.setrecursionlimit(10000)

################################
#INITIALIZING
mixer.init()  
master = tk.Tk()           
master.title('Phantom Player')
master.config(cursor='trek')
master.geometry('780x380') 

#Configuration
master.iconbitmap("IMages\icon.ico")
img1=Image.open("Images\\3.jpg")
img2=ImageTk.PhotoImage(img1)
img3=Image.open("Images\\6.jpg")
img4=ImageTk.PhotoImage(img3)
img5=Image.open("Images\\7.jpg")
img6=ImageTk.PhotoImage(img5)
pic=tk.Label(master,image=img2,width=780,height=380)
pic.place(x=0,y=0)
ltitle=Label(master, text='Song Name',bg='gold',bd=5, wraplength=200, font='ariel 20 bold')
ltitle.place(x = 300 , y = 25)
vol = 'VOL'
lvol=Label(master,width = 5,height=2, text=vol,bg='red',foreground = 'black',bd=5, font = 'ariel 17 bold')
lvol.place(x = 347 , y = 190)


n = 0.5#initilizing value of volume

################################
#MAKING FUNCTIONS

def play():
    mixer.music.play()
def pause():
    mixer.music.pause()
def stop():
    mixer.music.stop()
def resume():
    mixer.music.unpause()
def select():
    global songname
    mixer.music.stop()
    songname = askopenfilename() #K:/Music/ Kaer Morhen.mp3
    mixer.music.load(songname)   #song1 = ['K:/Music','Kaer Morehn.mp3]
    mixer.music.set_volume(n)
    song1 = songname.rsplit('/',1)[1] #song = ['KAER mORHEN','mp3']
    song = song1.rsplit('.',1)[0] #song = Kaer Morhen
    v = (int(n*100))
    vol = (v,'%') #50%
    ltitle.configure(text = song)
    lvol.config(text=vol)
def up():
    global n
    n = n + 0.05 #n = 0.5+0.05
    if n > 1: #n >100
        n = 1
    mixer.music.set_volume(n) 
    v = (int(n*100))
    vol = (v,'%')
    lvol.config(text=vol)
    
def down():
    global n
    n = n - 0.05
    if n < 0:
        n = 0
    mixer.music.set_volume(n) 
    v = (int(n*100))
    if v < 0:
        v = 0
    vol = (v,'%')
    lvol.config(text=vol)

def playlist_select():
    mixer.music.stop()
    song_select = askopenfilename() #song_select = K:/Music/Kaer Morhen.mp3
    fil = open('playlist.txt' , 'a') #'a' for append
    songx =  '\n' + song_select # \nK:/Music/Kaer Morhen.mp3
    fil.write(songx) #address is written on next line
    fil.close() #file is saved


def play_playlist(): #load button
    global s
    global songname
    fil = open('playlist.txt' , 'r') #reading a file
    strx = fil.read()
    s = strx.split('\n') #s = ['',K:/Music/Kaer Morhen.mp3','K:/Music/Never Fade Away.mp3',]
    if s[0] == '':
        del(s[0])          
    songname = s[0] #selecting song on index 0 of songs list
    mixer.music.load(songname)
    song1 = songname.rsplit('/',1)[1]#rsplit starts split from right side
    song = song1.rsplit('.')[0]      #1 in ('/',1) means to split from first '/'
    v = (int(n*100))                 #and[0] means first index
    vol = (v,'%')
    ltitle.configure(text = song)
    lvol.config(text=vol)

def prev():
    global song
    global songname
    indexx = s.index(songname) #getting index of currently running song
    if indexx == 0: #to create a circle of songs
        indexx  = len(s)
    mixer.music.stop()
    prev_song_index = ((indexx)-1)
    songname = s[prev_song_index] #assigning new song address to variable songname
    mixer.music.load(songname) 
    mixer.music.set_volume(n)
    song1 = songname.rsplit('/',1)[1]
    song = song1.rsplit('.')[0]
    v = (int(n*100))
    ltitle.configure(text = song)
    mixer.music.play()
def nextz():
    global song
    global songname
    indexx = s.index(songname)
    if indexx == len(s)-1: 
        indexx  = -1
    mixer.music.stop() #to stop current running music
    next_song_index = (indexx+1)
    songname = s[next_song_index]
    mixer.music.load(songname) 
    mixer.music.set_volume(n)
    song1 = songname.rsplit('/',1)[1]
    song = song1.rsplit('.')[0]
    v = (int(n*100))
    ltitle.configure(text = song)
    mixer.music.play()

def nonez():
    x = 'Hello G'

def autoplay():
    butresume.configure(command = nonez) #Disabling all other buttons to let program work correctly during autoplay
    butpause.configure(command = nonez)  #only volume button is available
    butplay.configure(command = nonez)
    butstop.configure(command = nonez)
    butselect.configure(command = nonez)
    butprev.configure(command = nonez)
    butnext.configure(command = nonez)
    butplayselect.configure(command = nonez)
    butplaylistplay.configure(command = nonez)
    butap.configure(command = nonez)
    play_playlist() #autoplay fucntion first loads the musix on the playlist
    autoplay_next() #then autplay calls this function to start songs on the playlist for autoplay
    

def autoplay_next(): #this function keeps calling itself again and again when a song stops and play next song automatically
    global song                                ########
    global songname                                   #
    indexx = s.index(songname)                        ##
    if indexx == len(s)-1:                            ###
        indexx  = -1                                  ####
    next_song_index = (indexx+1)                      ##### This is just
    songname = s[next_song_index]                     ##### copy of nextz
    mixer.music.load(songname)                        ##### button
    mixer.music.set_volume(n)                         ####
    song1 = songname.rsplit('/',1)[1]                 ###
    song = song1.rsplit('.')[0]                       ##
    v = (int(n*100))                                  #
    ltitle.configure(text = song)                     #
                                               ########
    mixer.music.play() #then starts playing the song
    song = MP3(songname) #to make it clear that song is MP3
    songlength = song.info.length #syntax to find length of song in sec
    songl = int(songlength)#converting length of song into integers
    length = songl*1000 #master.after asks miliseconds so making sec
    master.after(length+1000,autoplay_next) #1000 means adding one second more
   #master.after(time[mili second], function)
   #master.after adds an event to be run after time[miliseconds]
   #and it will be equal to length of song

################################################
#MAKING RGB

flag = True #Creating a variable with value True
def rgb(r, g, b): #Defining The Function
    global flag #Making the variable Flag Global else it gives some error
    sleep(15 / 1000) #as we need a delay of 0.015 seconds so we divide 15 by 1000
                        #sleep function stops the program on line 141 for 0.015 seconds
    master.update() #update is used to refresh mainloop 
    #Now we use configure to change colour of the Labels
    l1.configure(bg=f'#{r:02x}{g:02x}{b:02x}') #print('i am anas') , anas =5 ,  f'i am{anas}' i am 5
    #Now to understand the above line first understand formatting
        #f' ' is used for formatting which basically means nothing alone
        #now if we write anything in { } in f' ' it will be read as variable not a string
        #if you write print(f'x') it will print out x
        #But if you have a variable n=5 and you want to use it also in inverted commas
        #then you will write it is print(f'x{n}') it will print x5 instead of xn
    #Now basically lets take out f'#{r:02x}' from the above syntax
        #it means that print value of r and after colon 0 means to print a 0 before
        #number if if number is 1 digit,2 means that the digit must be 2 digit.
        #matlab ye k you need to print 02 instead of 2,03 instead of 3 and so on
        #if you use f'#{r:12x} then it will write 1 as 11, 2 as 12, 3 as 13 and so on
        #so now x means to convert resulting value into hexadecimal 
        #we need a hexadecimal number and like this f'#{r:02x}{g:02x}{b:02x}') gives us
        #a hexadecimal code with 6 characters where every 2 characters signify a colour
        #and 3 colours are needed to mix make a random new colour and # before this 
        #syntax is printed as it is before this is needed to show python that this is
        #a color code. so when (bg=f'#{r:02x}{g:02x}{b:02x}' runs first time it has
        #values r=0,b=0,g=0, so output of this syntax is like #000000 and this colour 
        #and it means any colour that is assigned to this color code
    #so all labels will get this colour
    l2.configure(bg=f'#{r:02x}{g:02x}{b:02x}')
    l3.configure(bg=f'#{r:02x}{g:02x}{b:02x}')
    l4.configure(bg=f'#{r:02x}{g:02x}{b:02x}')
    frame.configure(highlightbackground=f"#{r:02x}{g:02x}{b:02x}")
    #Now this statement will run as flag == True as stated earlier on line 133
    if flag:
        if (r != 255):
        #now first this if statement will run 
        #here master.after means to run the code as soon as master which is our mainloop refreshes
        #mainloop keeps refreshing so this if flag function keeps running.delay specifies for how much
        #second this loop should wait until until it runs again.as delay is equal to 5,it means 
        #to stop a color for 0.005 second.and after that it runss rgb function which is written
        #in master.after(delay, rgb, r+1, g, b) with parametres r+1,g,b and it runs until r is equal
        #to 255 ,after that g becomes increasing and so on until all 3 become equal to 255.
        #here 255 is max intensity of a colour.0 means white or black and 255 means brightest colour
            master.after(0, rgb, r+1, g, b)
        elif (g != 255):
            master.after(0, rgb, r, g+1, b)
        elif (b != 255):
            master.after(0, rgb, r, g, b+1)
        else:
            flag = False
            master.after(0, rgb, r, g, b)
        #now that all values of r,g,b are 255 so else statement will run flag becomes equal to False
        #now else condition will run
    if not flag:
        #in else condition just like first now first if condition will run and values will go 
        #on decreasing this time until all are equal to 0
        if (r != 0):
            master.after(0, rgb, r-1, g, b)
        elif (g != 0):
            master.after(0, rgb, r, g-1, b)
        elif (b != 0):
            master.after(0, rgb, r, g, b-1)
        #when all values of r,g,b  become equal to 0 then else will run and flag will become True
        #then again if flag condition will run and this fill go on forever
        #hope you guys understand, Anas
        else:
            flag = True
            master.after(0, rgb, r, g, b)
        #btw rgb function is called at the end

modex  = 0
def darkmode():
    global modex
    if modex == 0:
        modex = 1
        butresume.config(bg = 'mediumblue',foreground = 'black')
        butpause.config(bg = 'dodgerblue',foreground = 'black')
        butplay.config(bg = 'fuchsia',foreground = 'black')
        butstop.config(bg = 'springgreen',foreground = 'black')
        butselect.config(bg = 'salmon',foreground = 'black')
        butup.config(bg = 'midnightblue',foreground = 'black')
        butdown.config(bg = 'aqua',foreground = 'black')
        butprev.config(bg = 'darkviolet',foreground = 'black')
        butnext.config(bg = 'green',foreground = 'black')
        butplayselect.config(bg = 'gold',foreground = 'black')
        butplaylistplay.config(bg = 'gold',foreground = 'black')
        butap.config(bg = 'yellow',foreground = 'black')
        pic.config(image = img4)
        ltitle.config(bg = 'steelblue',foreground = 'black')
        lp.config(bg = 'tomato',foreground = 'black')
        lpp.config(bg = 'goldenrod',foreground = 'black')
        butmode.config(bg = 'orange',foreground = 'black')
        lvol.config(bg = 'red', foreground = 'black')


    elif modex  == 1:
        modex  = 2
        butresume.config(bg = 'black',foreground='blue')
        butpause.config(bg = 'black',foreground='blue')
        butplay.config(bg = 'black',foreground='blue')
        butstop.config(bg = 'black',foreground='blue')
        butselect.config(bg = 'black',foreground='cyan')
        butup.config(bg = 'black',foreground='lime')
        butdown.config(bg = 'black',foreground='lime')
        butprev.config(bg = 'black',foreground='yellow')
        butnext.config(bg = 'black',foreground='yellow')
        butplayselect.config(bg = 'black',foreground='deeppink')
        butplaylistplay.config(bg = 'black',foreground='deeppink')
        butap.config(bg = 'black',foreground='green')
        pic.config(image = img6)
        pic.config(width=780,height=380)
        ltitle.config(bg = 'black',foreground='white')
        lp.config(bg = 'black',foreground='cyan')
        lpp.config(bg = 'black',foreground='crimson')
        butmode.config(bg = 'black',foreground='springgreen')
        lvol.config(bg = 'black', foreground = 'orange')

    elif modex == 2:
        modex = 0
        butresume.config(bg = 'deepskyblue',foreground = 'black')
        butpause.config(bg = 'deepskyblue',foreground = 'black')
        butplay.config(bg = 'cyan',foreground = 'black')
        butstop.config(bg = 'cyan',foreground = 'black')
        butselect.config(bg = 'hotpink',foreground = 'black')
        butup.config(bg = 'lawngreen',foreground = 'black')
        butdown.config(bg = 'lawngreen',foreground = 'black')
        butprev.config(bg = 'darkgray',foreground = 'black')
        butnext.config(bg = 'darkgray',foreground = 'black')
        butplayselect.config(bg = 'cornflowerblue',foreground = 'black')
        butplaylistplay.config(bg = 'cornflowerblue',foreground = 'black')
        butap.config(bg = 'lightgreen',foreground = 'black')
        pic.config(image = img2)
        pic.config(width=780,height=380)
        ltitle.config(bg = 'gold',foreground = 'black')
        lp.config(bg = 'crimson',foreground = 'black')
        lpp.config(bg = 'royalblue',foreground = 'black')
        butmode.config(bg = 'orange',foreground = 'black')
        lvol.config(bg = 'red', foreground = 'black')


#################################
#MAKING BUTTONS

colors = ['lime','deeppink','yellow','red','blue']

frame = Frame(master)
frame.config(highlightbackground='blue',highlightthickness=10)

butresume = tk.Button(frame,text= u"\u23ef", width=10,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='deepskyblue',font='calibri', bd ='6', command = resume) 
butpause = tk.Button(frame, text= u"\u23f8", width=10,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='deepskyblue',font='calibri', bd ='6', command = pause) 
butplay = tk.Button(frame, text= u"\u23f5", width=10,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='cyan',font='calibri', bd ='6', command = play) 
butstop = tk.Button(frame, text= u"\u23f9", width=10,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='cyan',font='calibri', bd ='6', command = stop) 
butselect = tk.Button(master, text= 'Select', width=5,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='hotpink',font='calibri', bd ='6', command = select) 
butup = tk.Button(master, text=u'\u25B2', width=15,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='lawngreen',font='calibri', bd ='6', command = up) 
butdown = tk.Button(master, text=u'\u25BC', width=15,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='lawngreen',font='calibri', bd ='6', command = down) 
butprev = tk.Button(master, text= u"\u23ee", width=7,height=2,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='darkgray',font='calibri', bd ='6', command = prev) 
butnext = tk.Button(master, text= u"\u23ed", width=7,height=2,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='darkgray',font='calibri', bd ='6', command = nextz) 
butplayselect = tk.Button(master, text= "Select", width=5,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='cornflowerblue',font='calibri', bd ='6', command = playlist_select) 
butplaylistplay = tk.Button(master, text= "Load", width=5,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='cornflowerblue',font='calibri', bd ='6', command = play_playlist) 
butap = tk.Button(master, text= 'AutoPlay', width=7,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='lightgreen',font='calibri', bd ='5', command = autoplay) 
butmode = tk.Button(master, text= 'Mode', width=7,height=1,activeforeground='black', activebackground=colors[random.randint(0,4)],bg='orange',font='calibri', bd ='5', command = darkmode) 

#################################
#MAKING LABELS

lp = Label(master,text = 'Song', bg = 'crimson', height =1 ,width =10,font = 40)
lp.place(x=15, y=24)
lpp = Label(master,text = 'PlayList', bg = 'royalblue', height =1 ,width =10,font = 40)
lpp.place(x=648, y=24)

#################################
#MAKING AND PLACING RGB LABELS

l1=Label(master,bg='blue',height = 26,width=1)
l1.place(x = 0 , y = 0) 
l2=Label(master,bg='blue',height = 26,width=1)
l2.place(x = 767 , y = 0) 
l3=Label(master,bg='blue',height = 1,width=110)
l3.place(x = 0 , y = 365) 
l4=Label(master,bg='blue',height = 1,width=110)
l4.place(x = 0 , y = 0)

 
########################################
#PLACING BUTTONS

butplayselect.place(x=695, y=58)
butplaylistplay.place(x = 695, y = 108)
butselect.place(x=15, y=58)
butprev.place(x=82, y=182)
butnext.place(x=607, y=182)
butup.place(x =175, y = 200)
butdown.place(x = 432, y =200)
butap.place(x=675,y=313)
butmode.place(x = 15, y =315)

frame.place(x=142, y=270)

butplay.pack(side = LEFT)
butresume.pack(side = LEFT)
butpause.pack(side = LEFT)
butstop.pack(side = LEFT)

############################

# this removes the maximize button
master.resizable(0,0)
#RUNNING RGB AND MAINLOOP
def shazel():
    mixer.music.stop()
    master.destroy()
master.protocol('WM_DELETE_WINDOW', shazel)


rgb(0,0,0)
master.mainloop()


#THE END