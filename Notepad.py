from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))


if __name__ == '__main__':
  
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x644")

    
    TextArea = Text(root, font="lucida 10")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    
    MenuBar = Menu(root)

    #File Menu 
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New     Ctrl+N", command=newFile)
    FileMenu.add_command(label="Open   Ctrl+O", command = openFile)
    FileMenu.add_command(label = "Save     Ctrl+S", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit       Ctrl+Q", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
  

    #Edit Menu 
    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label = "Cut      Ctrl+X", command=cut)
    EditMenu.add_command(label = "Copy   Ctrl+C", command=copy)
    EditMenu.add_command(label = "Paste   Ctrl+V", command=paste)
    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    root.config(menu=MenuBar)

    #Scrollbar 
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
