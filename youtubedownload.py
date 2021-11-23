from tkinter import *
from tkinter import ttk 
from tkinter import filedialog
from pytube import YouTube
import tkinter as tk
from tkinter.ttk import Combobox

from pytube.extract import video_id

# "Youtube Video Downloader" başlıklı 500x300 bir pencere oluşturdum.
window = Tk()
window.geometry('500x300')
window.resizable(0,0)
window.title("YouTube Video Downloader")
window.columnconfigure(0,weight=1)
window.config(bg="gray3")#arkaplan

#Pencerede bir başlık oluşturdum.
Label(window,text = 'Youtube Video Downloader', font ='arial 20 bold',background="gray3",fg="orange").pack()

#Bağlantı girmek için bir alan oluşturdum.
link = StringVar()
Label(window, text = 'Linkinizi buraya yapıştırın:', font = 'arial 15 bold',background="gray3",fg="orange").place(x= 120 , y = 60)
link_enter = Entry(window, width = 70,textvariable = link).place(x = 33, y = 90)


#İndirmek için işlev oluşturdum.

#video = None
def Downloader():
    #global video

    #important
    url =YouTube(str(link.get()))
    secim = variable.get()
    
    
    if(secim == values[0]):
        video = url.streams.filter(progressive=True, res='720p')
        
        
        

    elif(secim == values[1]):
        video = url.streams.filter(progressive=True, res='144p')
       
      

    elif(secim == values[2]):
        video = url.streams.filter(progressive=False, type='audio').first()
        
       
    
       #https://www.youtube.com/watch?v=w7dBRJnxTUo

     
    # video nereye indirilsin
    nereye_indireyim = filedialog.askdirectory()
    video.download(output_path=nereye_indireyim)


  #indirildikten sonraki bildirim
    Label(window, text = 'Videonuz Başarıyla İndirildi', font = 'arial 15',background="gray3",fg="Green").place(x= 125 , y = 240)

    #indirme butonu.
Button(window,text = 'İNDİR', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 30, command = Downloader).place(x=185 ,y = 180)

#combobox seçenekleri
variable = tk.StringVar()
variable.set("Video Kalitesini Seçiniz")
values = ["720p","144p","Sadece Ses"]
combobox = Combobox(master=window,textvariable=variable,values=values,).place(x= 175 , y = 135)

window.mainloop()
