from tkinter import *
from click import command
from pytube import YouTube
root = Tk()
root.geometry('400x200')
root.resizable(100,100)
root.title("YouTube Downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()


link = StringVar()
Label(root, text = 'Enter download link:', font = 'arial 12 italic').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'dark gray', padx = 2, command = Downloader).place(x=180 ,y = 150)
# button=Button(root,text='Cancel', font = 'Timesnewroman 10 bold ', bg = 'blue', padx = 10)
# button.pack()
root.mainloop()
