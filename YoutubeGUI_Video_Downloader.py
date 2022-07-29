from tkinter import *
from pytube import YouTube

window = Tk()
Display = Label(window, text="DUNCAN'S VIDEO DOWNLOADER \n Enter Video link to Download!!!",
                font=("Times New Roman", 14, "bold"), padx=30, pady=30)
Display.pack()
window.title("DOWNLOADER")
url = StringVar()
Label(window, text="Enter video link to download", font=("Times New Roman", 14, "bold"), padx=20, pady=30)
entry_field = Entry(window, textvariable=url, width=200)
entry_field.place(x=50, y=100)


def Clicked():
    Link = entry_field.get()
    yt = YouTube(str(Link))
    video = yt.streams.get_highest_resolution()
    video.download(r"C:\Users\user\Desktop\ADS")
    Label(window, text='DOWNLOADED', font='arial 15').place(x=180, y=210)


button = Button(window, text="DOWNLOAD", font=("Times New Roman", 14, "bold"), command=Clicked)
button.pack()

window.mainloop()
