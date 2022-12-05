
from tkinter import *
from pytube import YouTube
import os

root = Tk()
root.geometry('300x300')
root.resizable(0,0)
root.configure(bg='#C80000')
root.title("Download from youtube")

Label(root, 
	text = 'YOUTUBE', 
	font ='roboto 18 bold', 
	fg = '#fff', 
	bg = '#C80000').place(x = 90, y = 40)

Label(root, 
	text = 'DOWNLOADER', 
	font ='roboto 18 bold', 
	fg = '#fff', 
	bg = '#C80000').place(x = 70, y = 70)

link = StringVar()

#input
userLink = Entry(root, 
	width = 30, 
	font = 'Roboto 11', 
	textvariable = link)
userLink.insert(END, ' Enter your link here ')
userLink.pack(padx = 40, pady = 130)

#buttons
def video():     
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, 
    	text = 'Your download is done!', 
    	font = 'roboto 12', 
    	fg = '#fff').place(x= 40 , y = 210)

def music():
    yt = YouTube(str(link.get()))
    convert = yt.streams.filter(only_audio=True).first()
    musicFile = convert.download()
    name, ext = os.path.splitext(musicFile)
    newFile = name + '.mp3'
    os.rename(musicFile, newFile)
    Label(root, 
    	text = 'Your download is done!', 
    	font = 'roboto 12', 
    	bg = '#C80000', 
    	fg = '#fff').place(x= 70 , y = 260)

# call function
Button(root,text = 'Music', 
	font = 'roboto 13 bold', 
	fg = '#fff', 
	bg = '#000', 
	padx = 2, command = music).place(x=70 ,y = 180)
Button(root,text = 'Video', 
	font = 'roboto 13 bold', 
	fg = '#fff', 
	bg = '#000', 
	padx = 2, command = video).place(x=150 ,y = 180)

#show me the window
root.mainloop()