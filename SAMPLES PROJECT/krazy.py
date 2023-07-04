#import library
from tkinter import *
from pytube import YouTube
#creating window
root = Tk()
#setting width and height of window
root.geometry('500x250')
#title for window
root.title("Krazyprogrammer presents")
#set background color
root["bg"]="#D55B06"
#Label for heading
Label(root,text = 'Krazy Youtube Video Downloader', font ='arial 18 bold',fg="white",bg="#D55B06").pack()
#declaring variable
link = StringVar()
#label for heading
Label(root, text = 'Paste video Link Here:', font = 'arial 15 bold',bg="#D55B06").place(x= 160 , y = 60)
#textbox/entrybox for getting link of video
link_enter = Entry(root, width = 60,textvariable = link).place(x = 72, y = 90)
#function for downloading
def YouTubeDownloader():
    #applying validation
    if link.get()!="":
     #getting url
     url =YouTube(str(link.get()))
     video = url.streams.first()
     #download video
     video.download()
     #show messsage
     Label(root, text = 'Video is downloaded successfully', font = 'arial 15',bg="#D55B06",fg="white").place(x= 70 , y = 210)
    else:
        Label(root, text='Link is empty', font='arial 15',bg="#D55B06",fg="white").place(x=180, y=210)
#button for download
Button(root,text = 'Download', font = 'arial 15 bold' ,bg = 'red',fg="white", padx = 1, command = YouTubeDownloader).place(x=180 ,y = 150)
#Run Application
root.mainloop()