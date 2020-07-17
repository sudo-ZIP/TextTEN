import tkinter
import os
import tkinter.font as tkFont
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *


class Notepad:

    __root = Tk()

    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root, font='Meiryo')
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None


    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    iconfile ='icon.ico'
    __root.iconbitmap(default=iconfile)
    #アイコンを読み込み

    def __init__(self,**kwargs):

        try:
                self.__root.wm_iconbitmap("Notepad.ico") #GOT TO FIX THIS ERROR (ICON)
        except:
                pass

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        #set the window text
        self.__root.title("Untitled - TextTEN")

        #center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        self.__thisTextArea.grid(sticky=N+E+S+W)

        self.__thisFileMenu.add_command(label="新規作成",command=self.__newFile)
        self.__thisFileMenu.add_command(label="開く",command=self.__openFile)
        self.__thisFileMenu.add_command(label="保存",command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="終了",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="ファイル",menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="カット",command=self.__cut)
        self.__thisEditMenu.add_command(label="コピー",command=self.__copy)
        self.__thisEditMenu.add_command(label="貼付け",command=self.__paste)
        self.__thisMenuBar.add_cascade(label="編集",menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="このTextTENについて",command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="ヘルプ",menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)


    def __quitApplication(self):
        self.__root.destroy()
        #exit()

    def __showAbout(self):
        showinfo("このTextTENについて","TextTEN Version1.0\n作成者 ZIP©\nブログ https://www.muryobochi.ml")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.__file == "":
            #no file to open
            self.__file = None
        else:
            #try to open the file
            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - TextTEN")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - TextTEN")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)

    def __saveFile(self):

        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                #try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                #change the window title
                self.__root.title(os.path.basename(self.__file) + " - TextTEN")

        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<カット>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<コピー>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<貼付け>>")

    def run(self):

        self.__root.mainloop()

notepad = Notepad(width=600,height=400)
notepad.run()