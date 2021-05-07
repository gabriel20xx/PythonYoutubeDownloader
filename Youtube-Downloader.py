import os
os.system('cmd /c pip --quiet --disable-pip-version-check --no-python-version-warning install pytube')

from pytube import YouTube
import tkinter as tk

root = tk.Tk()
root.title("Video Downloader")
root.geometry("950x150")

link_var = tk.StringVar()
location_var = tk.StringVar()


def submit():
    link = link_entry.get()
    location = location_entry.get()

    yt = YouTube(link)

    print(" ")
    print("Titel: ", yt.title)
    print("Autor: ", yt.author)
    print("Anzahl Aufrufe: ", yt.views)
    print("Länge des Videos: ", yt.length, " Sekunden")
    print("Bewertung des Videos: ", yt.rating, " Sterne")

    ys = yt.streams.get_highest_resolution()

    print("Downloading...")
    ys.download(location)

    frame1 = tk.Tk()
    frame1.title("Download completed!!")
    frame1.geometry("600x250")
    frame2 = tk.Label(frame1, text='Download completed!!', font=('calibre',  40, 'bold'), fg="green").pack(side="top")
    frame3 = tk.Button(frame1, text='Close', font=('calibre', 12, 'bold'), fg='black',
                       command=lambda: [frame1.destroy()], height=3, width=20).pack(side="bottom", pady=5)
    frame4 = tk.Button(frame1, text='Open', font=('calibre', 12, 'bold'), fg='black',
                       command=lambda: [frame1.destroy(), open(location)], height=3, width=20).pack(side="bottom", pady=5)


    def open(location):
        from os import startfile
        startfile('"' + location + yt.title + '.mp4"')

#   frame2.grid(row=0, column=1)
#   frame3.grid(row=1, column=1)
#   frame4.grid(row=2, column=1)

    print("Download completed!!")

    root.destroy()

    link_var.set("")
    location_var.set("")


link_label = tk.Label(root, text='Link: ', font=('calibre',  20, 'bold'))
link_entry = tk.Entry(root, textvariable=link_var, font=('calibre', 20, 'normal'), width=50)

location_label = tk.Label(root, text='Speicherort: ', font=('calibre',  20, 'bold'))
location_entry = tk.Entry(root, textvariable=location_var, font=('calibre', 20, 'normal'), width=50)

submit = tk.Button(root, text='Download', font=('calibre', 12, 'bold'), fg='green', command=submit, height=3, width=20)

link_label.grid(row=0, column=0)
link_entry.grid(row=0, column=1)
location_label.grid(row=1, column=0)
location_entry.grid(row=1, column=1)
submit.grid(row=2, column=1)

root.mainloop()
