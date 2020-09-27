from tkinter import *
from tkinter import filedialog
from googleImageCrawling import googleCrawl

def ask():
    root.dirName = filedialog.askdirectory()
    print(root.dirName)
    txt1.configure(text= 'D/L path : ' + root.dirName)


def askFile():
    root.fileName = filedialog.askopenfilename()
    print(root.fileName)
    txt2.configure(text= 'Chorome Driver path : ' + root.fileName)

def start():
    # print(identry.get())
    # print(pwentry.get())
    # print(queryentry.get())
    # print(root.dirName)
    # print(root.fileName)
    googleCrawl(root.dirName, root.fileName, identry.get(), pwentry.get(), queryentry.get())
    # 여러개 검색어로 하려면 검색어를 여러개 받아서 리스트로 만든다음에 포문 돌려서 하면 될듯
    


root = Tk()
root.title("Google Image Crawler")
root.geometry("540x300+100+100")
root.resizable(False, False)

# btn.grid(row=1, column=1)
idLabel = Label(root, text='G-mail :')
idLabel.pack()
identry = Entry(root) 
identry.pack()

pwLabel = Label(root, text='Password :')
pwLabel.pack()
pwentry = Entry(root, show='*') 
pwentry.pack()

queryLabel = Label(root, text='Keyword :')
queryLabel.pack()
queryentry = Entry(root)
queryentry.pack()



txt1 = Label(root, text='Download path : ')
txt1.pack()
# txt.grid(row=1, column=0)

btn = Button(root, text="Select path", command=ask)
btn.pack()

txt2 = Label(root, text='Chrome driver path : ')
txt2.pack()
# txt.grid(row=1, column=0)

btn = Button(root, text="Select path", command=askFile)
btn.pack()


playbtn = Button(root, text='Start', command=start)
playbtn.pack()

root.mainloop()
