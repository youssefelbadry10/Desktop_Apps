from  tkinter import *
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube

root = Tk()
root.title("Youtube Downloader ")
root.geometry("700x400")
root.resizable(FALSE,FALSE)


def browse():
    choose_file = filedialog.askdirectory(title= "Save video")
    folderentry.delete(0, "end")
    folderentry.insert(0, choose_file)

def downnload():
    status.config(text="Status : Downloding..... " )
    link= yt_entry.get()
    folder = folderentry.get()
    YouTube(link, on_complete_callback=finish).streams.filter(progressive=True, file_extension="mp4").desc().first().download(folder)

def finish(stream=None, chunk= None, file_handle=None, remaining= None):
    status.config(text="Status : Complete ")
#Youtube logo

logo = PhotoImage(file="png-transparent-youtube-logo-music-video-computer-icons-youtube-logo-text-trademark-logo.png").subsample(2)
title = Label(root, image=logo)
title.place(relx=0.5, rely= 0.25 , anchor="center")

#youtube link

yt_label = Label(root, text="Youtube Link")
yt_label.place(x=25, y=180)

yt_entry = ttk.Entry(root, width=60)
yt_entry.place(x=140, y=180)

#Download_folder

folderlabel = Label(root, text="Download Folder")
folderlabel.place(x=25, y=230)

folderentry = ttk.Entry(root, width=50)
folderentry.place(x=140, y=230)

#Browse button

browse = ttk.Button(root, text="Browse", command=browse)
browse.place(x=455, y= 230)

#Download button

download = ttk.Button(root, text="Download ", command=downnload)
download.place(x=280, y=280)

#Status

status = Label(root, text="Status : Ready", font="calibre 10 italic ")
status.place(rely=1 , anchor="sw", relwidth=1)
root.mainloop()