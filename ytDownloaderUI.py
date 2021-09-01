import tkinter as tk
from tkinter import *
import ytDownloader

#Create window object
window = tk.Tk()
window.title("Youtube Video Downloader")
window.columnconfigure(0, weight=1, minsize=250)
window.rowconfigure([0, 1], weight=1, minsize=100)


#Create Frames
topFrame = tk.Frame(master = window, relief=tk.SUNKEN, borderwidth=3)
topFrame.grid(row=0, column=0)


bottomFrame = tk.Frame(master = window,relief=tk.RAISED, borderwidth=3)
bottomFrame.grid(row=1, column=0)


#Create label
greeting = tk.Label(master = topFrame, text="Download any Youtube video!")
greeting.grid(row=0, column=1)

#Create Field Label
urlLabel = tk.Label(master = topFrame, text="Url:")
urlLabel.grid(row=1, column=0)

#Create entry field
entry = tk.Entry(master = topFrame, bg="grey", width=30)
entry.grid(row=1, column=1)



# Create radio buttons (CAN ADD FUNCTIONALITY LATER)
# quality = ["144p", "240p", "360p", "480p", "720p", "1080p"]
# qualityLabel = tk.Label(master = topFrame, text="Quality:")
# qualityLabel.grid(row=2, column=0)

# for colNum in range(1):
#     for rowNum in range(6):
#         radioLabel = tk.Label(master = topFrame, text=quality[rowNum])
#         radioLabel.grid(row=rowNum+3, column=colNum,  sticky="nsew")

#         radioButton1 = tk.Radiobutton(master= topFrame)
#         radioButton1.grid(row=rowNum+3,column=colNum+1,  sticky="nsew")


#Callback functions 
def downloadClick():
    url = entry.get()
    ytDownloader.download(url)

def exitWindow():
    window.destroy()

#Create buttons
downloadButton = tk.Button(master = bottomFrame,text="Download", command=downloadClick)
downloadButton.grid(row=0, column=0,  sticky="nsew")

exitButton = tk.Button(master = bottomFrame,text="Exit", command=exitWindow)
exitButton.grid(row=0, column=1,  sticky="nsew")


#Run the main event loop
window.mainloop()


