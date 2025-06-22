import os
import sys
from tkinter import *
from tkinter import messagebox
from pytube import YouTube

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def download_video():
    link = url.get().strip()
    if not link:
        messagebox.showerror("Error", "Please enter a YouTube video link.")
        return
    try:
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()
        # Change this to a user-writable path or ask user for a directory
        download_path = os.path.expanduser("~/Downloads")
        video.download(download_path)
        messagebox.showinfo("Success", f"Video downloaded to {download_path}")
    except Exception as e:
        messagebox.showerror("Download Failed", f"An error occurred:\n{e}")

window = Tk()
window.title("YouTube Video Downloader")
window.geometry("500x250")
window.resizable(False, False)

Label(window, 
      text="DUNCAN'S VIDEO DOWNLOADER\nEnter Video link to Download!!!",
      font=("Times New Roman", 14, "bold"),
      padx=30, pady=20
).pack()

url = StringVar()

Label(window, 
      text="Enter video link to download", 
      font=("Times New Roman", 12),
      padx=10
).pack()

entry_field = Entry(window, textvariable=url, width=50, font=("Arial", 12))
entry_field.pack(pady=10)

button = Button(window, text="DOWNLOAD", font=("Times New Roman", 14, "bold"), command=download_video)
button.pack(pady=10)

window.mainloop()
